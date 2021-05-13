from flask import Flask
from basic_function.connection_dbModel import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
