from app import User,Game,db
db.create_all()
user = User(username ='msj',password='123456')
db.session.add(user)
game1 = Game(gamename='王者荣耀',type='MOBA',userid=1)
game2 = Game(gamename='英雄联盟',type='MOBA',userid=1)
game3 = Game(gamename='原神',type='RPG',userid=1)
print(user,game1,game2,game3)

db.session.add(game1)   
db.session.add(game2)
db.session.add(game3)       
db.session.commit()
games = Game.query.all()

for game in games:
    print(game.id, game.gamename, game.type, game.userid)