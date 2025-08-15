from flask import Flask, request, jsonify
from markupsafe import escape
from flask import url_for

app = Flask(__name__)
@app.route('/')
def public_page():
    return 'Welcome to the public page!'
@app.route('/user/<username>')
def user_page(username):
    print(url_for('user_page', username=username))  # 打印URL
    return f'User: {escape(username)}'

