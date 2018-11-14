#!/usr/bin/python2.7
from flask import Flask
import platform
import sys
sys.path.insert(0, '/var/www/demo-app/app')

app = Flask(__name__)
app.config.from_object(__name__)
print "configuration finished"


@app.route('/')
def hello_world():
    return platform.node()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8090)
