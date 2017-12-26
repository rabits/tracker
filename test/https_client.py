#!/usr/bin/env python

import sys
import urllib, urllib2, base64

import ssl
import zlib

url = sys.argv[1]
auth = sys.argv[2]

line = '''[
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}},
{"something":[1,2,3,4,5],"other":true,"another":{"a":null}}
]'''
print len(line)
post_data = zlib.compress(line)
print len(post_data)

post_req = urllib2.Request(url)
post_req.add_header('Authorization', 'Basic ' + base64.b64encode(auth))
post_req.add_data(post_data)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urllib2.urlopen(post_req, context=ctx)
response_data = response.read()
response.close()

print response_data
