from flask import Flask, jsonify
myapp = Flask(__name__)


@myapp.route("/")
def hello():
    return "hello world"
