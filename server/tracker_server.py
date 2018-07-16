from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

import base64, hashlib
from hashlib import sha256
import zlib, json

from numbers import Number
from datetime import datetime
import time

# Encode date to appropriate json format
class DateTimeEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime):
            return time.mktime(value.timetuple()) + value.microsecond/1000000.0

        return json.JSONEncoder.default(self, value)

hashsalt = None
users = {}
db = None

class ServerHandler(BaseHTTPRequestHandler):
    '''Server class for basic auth, show some UI & receive the data'''
    def sendAuthRequest(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="No luck"')
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

    def checkAuth(self):
        global hashkey, hashsalt

        if self.headers.getheader('Authorization') == None:
            self.sendAuthRequest()
            self.wfile.write('no auth header received')
        else:
            user = users.get(sha256(sha256(self.headers.getheader('Authorization')).digest()+hashsalt).digest())
            if user != None:
                self._user = user
                return True
            else:
                self.sendAuthRequest()
                self.wfile.write(self.headers.getheader('Authorization'))
                self.wfile.write('not authenticated')

        return False

    def processAPIv1(self):
        req = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(req.query)
        path = req.path.split('/')[1:]
        out = {'result': 'error', 'message': ''}

        try:
            if path[2] == 'get':
                if path[3] == 'devices':
                    out['data'] = db.getDevices()
                    out['result'] = 'ok'
                elif path[3] == 'headers':
                    out['data'] = db.getHeaders(params['device_id'][0])
                    out['result'] = 'ok'
                elif path[3] == 'data':
                    out['data'] = db.getData(int(params['device_id'][0]), int(params['header_id'][0]), float(params['utime_from'][0]), float(params['utime_to'][0]))
                    out['result'] = 'ok'
        except Exception as e:
            out['message'] = "Unable to get the API path " + self.path
            out['exception'] = '%s: %s' % (e.__class__.__name__, e)
        finally:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(out, separators=(',',':'), cls=DateTimeEncoder))

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

    def do_GET(self):
        '''GET request response'''
        if not self.checkAuth():
            return

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as f:
                self.wfile.write(f.read())
        else:
            if self.path.startswith('/api/v1'):
                self.processAPIv1()
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write('ERROR: Unable to find the requested page')


    def do_POST(self):
        '''POST request response'''
        if not self.checkAuth():
            return

        out = {'result': 'error', 'message': ''}

        try:
            length = int(self.headers.get('Content-Length'))
            print length
            data = self.rfile.read(length)
            if self.headers.get('Content-Encoding') == 'gzip':
                data = zlib.decompress(data, 0)
            data = data.decode('utf-8')

            print len(data)
            print 'Data from: ' + self._user

            self._storeData(self._user, json.loads(data))

            out['result'] = 'ok'
        except Exception as e:
            out = {'result': 'error', 'message': 'Server exception: %s' % e}
            raise
        finally:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(out, separators=(',',':')))

    def _storeData(self, sender, data):
        # transam {"adc":{"1512950739443":{"Battery Voltage":11.97},"1512950709371":{"Battery Voltage":11.96},"1512950619157":{"Battery Voltage":11.96},"1512950649230":{"Battery Voltage":11.88},"1512950559015":{"Battery Voltage":null}}}
        for module, tdata in data.iteritems():
            db.storeData(sender, module, tdata)

class PostgreSQLStorage(object):
    def __init__(self, user, password, dbname='tracker', host='localhost', port=5432):
        self._cfg = {
            'user':user,
            'password':password,
            'dbname':dbname,
            'host':host,
            'port':port
        }

        self._c = None

        self._tables = {} # Cache for tables
        self._headers = {} # Cache for headers
        self._devices = {} # Cache for devices
        self._updateTable()
        self._prepareTables()

        print 'PostgreSQL Storage: Init done'

    def _connect(self):
        if not self._c or self._c.closed != 0:
            print 'Connecting to the DB'
            import psycopg2, psycopg2.extras
            self._cfg['connection_factory'] = psycopg2.extras.RealDictConnection
            self._c = psycopg2.connect(**self._cfg)

    def _updateTable(self, table_name = None):
        self._connect()

        cur = self._c.cursor()
        sql = 'SELECT table_name, column_name, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name '
        if table_name:
            sql += cur.mogrify('= %s', [table_name])
        else:
            sql += cur.mogrify('IN (SELECT tablename FROM pg_catalog.pg_tables WHERE tableowner = %s)', [self._cfg['user']])

        cur.execute(sql + ';')

        data = cur.fetchall()
        out = {}
        for column in data:
            if not out.has_key(column['table_name']):
                out[column['table_name']] = {}
            out[column['table_name']][column['column_name']] = column['data_type']
        self._tables.update(out)

    def _createTable(self, name, spec):
        if self._tables.has_key(name):
            for col in spec:
                t = 'integer' if col['type'] == 'serial' else col['type']
                dbtype = self._tables[name].get(col['name'])
                if dbtype != t:
                    raise Exception('ERROR: Wrong table "%s" existing in the database (column "%s" type "%s" but should be "%s")' % (name, col['name'], dbtype, t))
            return # Table exising in the db and spec is good

        print 'Creating a new table %s' % (name)
        sql = 'CREATE TABLE %s (' % name
        columns = []
        for col in spec:
            t = col['type']
            if col.get('length'):
                t += '(%d)' % col.get('length')
            s = '%s %s' % (col['name'], col['type'])
            columns.append(s)

        columns[0] += ' PRIMARY KEY'
        sql += ','.join(columns) + ');'

        self._connect()
        cur = self._c.cursor()
        cur.execute(sql)
        self._c.commit()

        self._updateTable(name)

    def _prepareTables(self):
        '''Will prepare control tables'''

        # device table
        self._createTable('device', [
            {'name': 'id', 'type': 'serial'},
            {'name': 'name', 'type': 'character varying', 'length': 128},
            {'name': 'description', 'type': 'text'},
        ])

        # header table
        self._createTable('header', [
            {'name': 'id', 'type': 'serial'},
            {'name': 'device_id', 'type': 'integer'},
            {'name': 'parent_id', 'type': 'integer'},
            {'name': 'name', 'type': 'character varying', 'length': 256},
            {'name': 'description', 'type': 'text'},
        ])

        # annotation table
        self._createTable('annotation', [
            {'name': 'id', 'type': 'serial'},
            {'name': 'device_id', 'type': 'integer'},
            {'name': 'time', 'type': 'timestamp without time zone'},
            {'name': 'description', 'type': 'text'},
        ])

    def _createDevice(self, name):
        if self._devices.has_key(name):
            return self._devices[name]

        self._connect()
        cur = self._c.cursor()
        cur.execute('SELECT id FROM device WHERE name = %s', [name])
        data = cur.fetchone()
        if data:
            self._devices[name] = data['id']
            return data['id']

        cur.execute('INSERT INTO device (name) VALUES (%s) RETURNING id;', [name])
        row_id = cur.fetchone()
        self._c.commit()
        self._devices[name] = row_id
        return row_id

    def _createHeader(self, device_id, name, parent_id = None):
        cid = '{}{}{}'.format(device_id, parent_id, name)
        if self._headers.has_key(cid):
            return self._headers[cid]

        self._connect()
        cur = self._c.cursor()
        cur.execute('SELECT id FROM header WHERE device_id = %s AND parent_id {} %s AND name = %s'.format('=' if parent_id else 'is'), [device_id, parent_id, name])
        data = cur.fetchone()
        if data:
            self._headers[cid] = data['id']
            return data['id']

        print cur.mogrify('Creating new header: %s %s %s', [device_id, parent_id, name])
        cur.execute('INSERT INTO header (device_id, parent_id, name) VALUES (%s, %s, %s) RETURNING id;', [device_id, parent_id, name])
        row_id = cur.fetchone()
        self._c.commit()
        self._headers[cid] = row_id
        return row_id

    def getDevices(self):
        self._connect()

        cur = self._c.cursor()
        try:
            cur.execute('SELECT * FROM device')
            data = cur.fetchall()
            return data
        except:
            self._c.rollback()
            raise

    def getHeaders(self, device_id):
        self._connect()

        cur = self._c.cursor()
        try:
            # Selecting headers with data types of values
            cur.execute("""SELECT header.*, data_type FROM header
                    LEFT OUTER JOIN information_schema.columns ON concat('data_', device_id, '_', id) = table_name AND column_name = 'value'
                    WHERE device_id = %s ORDER BY id ASC""", [device_id])
            data = cur.fetchall()
            return data
        except:
            self._c.rollback()
            raise

    def getData(self, device_id, header_id, utime_from, utime_to):
        self._connect()

        table = 'data_%d_%d' % (device_id, header_id)
        cur = self._c.cursor()
        try:
            cur.execute('SELECT * FROM {} WHERE "time" >= %s AND "time" <= %s ORDER BY time ASC'.format(table), [datetime.fromtimestamp(utime_from), datetime.fromtimestamp(utime_to)])
            data = cur.fetchall()
            return data
        except:
            self._c.rollback()
            raise

    def storeData(self, device, name, time_data):
        '''Processing one time record from a module, prepares tables and data to send'''
        print 'Device %s storing data for module %s (%d)' % (device, name, len(time_data))
        device_id = self._createDevice(device)
        header_id = self._createHeader(device_id, name)

        # Preparing data & tables in the DB
        tables = {}
        for time, data in time_data.iteritems():
            out = self._prepareTData(device_id, header_id, time, data)
            for t in out:
                tables[t] = tables.get(t, []) + [out[t]]

        # Storing data in the tables
        for table in tables:
            print 'Device %s storing data in table %s (%d)' % (device, table, len(tables[table]))
            cur = self._c.cursor()
            header = 'INSERT INTO %s (time, value) VALUES ' % table
            for i in xrange(0, len(tables[table]), 100):
                print '  Processing data [%s:%s] from %s' % (i, i+100, len(tables[table]))
                data = [ cur.mogrify('(%s, %s)', val) for val in tables[table][i:i+100] ]
                try:
                    cur.execute(header + ','.join(data) + ';')
                except Exception as e:
                    print 'Found exception while performing sql query: %s: %s' % (e.__class__.__name__, e)
                    print 'Processing the records one-by-one...'
                    self._c.rollback()
                    for n in xrange(i, min(i+100, len(tables[table]))):
                        try:
                            cur.execute(header + '(%s, %s);', tables[table][n])
                            self._c.commit()
                        except Exception as e:
                            print '  Unable to insert value %s: %s: %s' % (n, e.__class__.__name__, e)
                            self._c.rollback()

                self._c.commit()

    def _prepareTData(self, device_id, header_id, time, data):
        # data_[device_id]_[header_id] table: time, value (types: boolean, real, char(256))

        if isinstance(data, dict):
            out = {}
            for name, subdata in data.iteritems():
                o = self._prepareTData(device_id, self._createHeader(device_id, name, header_id), time, subdata)
                out.update(o)
            return out

        value = {'name': 'value'}
        if isinstance(data, bool):
            value.update({'type': 'boolean'})
        elif isinstance(data, Number):
            value.update({'type': 'real'})
        elif isinstance(data, str):
            value.update({'type': 'character varying', 'length': 256})
        else:
            # Who cares about null?
            return {}

        table = 'data_%d_%d' % (device_id, header_id)
        self._createTable(table, [
            {'name': 'time', 'type': 'timestamp without time zone'},
            value,
        ])

        return {table: [datetime.fromtimestamp(int(time)/1000.0), data]}

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) < 3:
        print 'Usage: python tracker_server.py <port> <username:password>[ username:password [...]]'
        sys.exit()
    hashsalt = os.urandom(32)
    for i in xrange(2, len(sys.argv)):
        users[sha256(sha256('Basic ' + base64.b64encode(sys.argv[i])).digest()+hashsalt).digest()] = sys.argv[i].split(':')[0]
    server = HTTPServer(('', int(sys.argv[1])), ServerHandler)
    try:
        db = PostgreSQLStorage(host='<CHANGEME_HOSTNAME>', port=5432, dbname='<CHANGEME_DBNAME>', user='<CHANGEME_USER>', password='<CHANGEME_PASSWORD>')
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
