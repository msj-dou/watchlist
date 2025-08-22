from flask import Flask, request, jsonify,render_template
from markupsafe import escape
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
import os
import click

prefix = 'sqlite:///'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    users = User.query.get(2)
    if users:
        username = users.username
        games = Game.query.filter_by(userid=users.id).all()
    else:
        username = '游客'
        games = []
    return render_template('index.html', games=games)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamename = db.Column(db.String(20), nullable=False) 
    type = db.Column(db.String(20), nullable=False)
    userid = db.Column(db.Integer,nullable=False)
                       
@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    if drop:
        db.drop_all()
    
    db.create_all()
    click.echo('Initialized database.') 

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'Grey Li'
    user = User(username=name,password='123')
    db.session.add(user)
    db.session.commit()
    games = [
        {'gamename': 'My Neighbor Totoro', 'type': '1988', 'userid': user.id},
        {'gamename': 'Dead Poets Society', 'type': '1989', 'userid': user.id},
        {'gamename': 'A Perfect World', 'type': '1993', 'userid': user.id},
        {'gamename': 'Leon', 'type': '1994', 'userid': user.id},
        {'gamename': 'Mahjong', 'type': '1996', 'userid': user.id},
        {'gamename': 'Swallowtail Butterfly', 'type': '1996', 'userid': user.id},
        {'gamename': 'King of Comedy', 'type': '1999', 'userid': user.id},
        {'gamename': 'Devils on the Doorstep', 'type': '1999', 'userid': user.id},
        {'gamename': 'WALL-E', 'type': '2008', 'userid': user.id},
        {'gamename': 'The Pork of Music', 'type': '2012', 'userid': user.id}
    ]

    
    for m in games:
        game = Game(gamename=m['gamename'], type=m['type'], userid=m['userid'])
        db.session.add(game)

    db.session.commit()
    click.echo('Done.')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.context_processor
def inject_user():
    user = User.query.first()
    if user:
        return dict(username=user.username)
    return dict(username='游客')