from flask import Flask, request, jsonify

app = Flask(__name__)

def hello():
    return "Hello, World!"