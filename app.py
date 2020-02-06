# -*- coding: utf-8 -*-
"""
    :author: Nicholas Kobzar
    :repo: https://github.com/n-g-s/simple-app.git
"""

from timer import timer
from flask import Flask, Response, jsonify, make_response


app = Flask(__name__)
MESSAGE = "Hello world"


@app.route('/')
def index():
    return Response(MESSAGE, mimetype="text/plain")


@app.route('/status/alive')
def liveness():
    response = Response(status=200)
    return response


@app.route('/status/ready')
def readiness():
    data = timer.app_readiness()
    return make_response(jsonify(data[0]), data[1])


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
