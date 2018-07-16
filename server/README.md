Tracker Server
==============

Receiver, storage & viewer of the data (logs, events) from the Tracker client.

Designed to work as backend service of https frontend proxy with basic token auth.

Requirements
------------

* PostgreSQL database
* HTTPS frontend proxy (nginx)
* Python 2.7 and psycopg2 module with extras

Usage
-----

1. Install nginx server
2. Copy nginx configuration virtual server configuration, setup it properly, restart nginx.
3. Change db connection `CHANGEME_*` access values in the `tracker_server.py` script
3. Run `tracker_service.py` with port & credentials like:
  ```
  $ python ./tracker_service.py 8235 <username>:<accesstoken>[ <username>:<accesstoken> ...]
  ```
4. Try to login to dashboard using your nginx service and check the logs
5. Setup tracker Client module on client side

TODO
----

* Add more db storge modules (MySQL, sqlite3, ...)
* Change config mechanism and move to tracker engine

Support
-------
If you like this project, you can support our open-source development by a small Bitcoin donation.

Bitcoin wallet: `15phQNwkVs3fXxvxzBkhuhXA2xoKikPfUy`
