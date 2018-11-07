from flask import Flask
import platform

app = Flask(__name__)
app.config.from_object(__name__)
print "configuration finished"


@app.route('/')
def hello_world():
    return platform.node()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)