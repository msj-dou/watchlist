from flask import Flask, request, jsonify,render_template
from markupsafe import escape
from flask import url_for

app = Flask(__name__)



@app.route('/')
def index():
    username = 'msj'
    games= [
            {'title':'动作','name':'奥德赛'},
            {'title':'大世界探索','name':'荒野之息'},
            {'title':'角色扮演','name':'巫师3'},
            {'title':'射击','name':'使命召唤'},
            {'title':'体育竞技','name':'FIFA23'}
    ]
    return render_template('index.html', username=username, games=games)
