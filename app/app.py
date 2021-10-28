"""
test application.
"""
import os
import socket
import pickledb # pylint: disable=import-error
from flask import Flask # pylint: disable=import-error
from redis import Redis # pylint: disable=import-error

# Connect to Redis
REDIS = Redis(host="redis", port=6379,
              db=0, socket_connect_timeout=2, socket_timeout=2)
# ...or a local (file-based) Pickle DB
PICKLE_DB = pickledb.load('/data/pysimple.db', True)

COUNTER_FIELD = 'counter'

APP = Flask(__name__)
VERSION = "0.23"


@APP.route("/")
def hello():
    """
    Try to use Redis
    and then fall-back to a pickle database...
    """
    try:
        visits = REDIS.incr(COUNTER_FIELD)
    except Exception as r_ex: # pylint: disable=broad-except
        print(f'WARNING: REDIS.incr({COUNTER_FIELD}) returned {r_ex}')
        try:
            visits = PICKLE_DB.get(COUNTER_FIELD)
        except Exception as p_ex: # pylint: disable=broad-except
            print(f'WARNING: PICKLE_DB.get({COUNTER_FIELD}) returned {p_ex}')
        # Initialise visits if we need to
        # and then increment
        if not visits:
            visits = 0
        visits += 1
        try:
            PICKLE_DB.set(COUNTER_FIELD, visits)
        except Exception as p_ex: # pylint: disable=broad-except
            print(f'WARNING: PICKLE_DB.set({COUNTER_FIELD}) returned {p_ex}')

    # visits should be set to something here,
    # either via a Redis increment or via a pickle-db instance,
    # or just a memory resident value.

    html = "Hello {name}!\n" \
           "Hostname: {hostname} \n" \
           "Num visits: {visits}\n" \
           "My version is {version}"
    return html.format(name=os.getenv("NAME", "world"),
                       hostname=socket.gethostname(), visits=visits, version=VERSION)


if __name__ == "__main__":

    # If I enable `debug=True` I get
    # `KeyError: 'getpwuid(): uid not found: 1000060000'` errors
    # from OpenShift.
    APP.run(host='0.0.0.0', port=8080)
