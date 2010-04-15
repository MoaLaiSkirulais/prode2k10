from google.appengine.ext import db

class Team(db.Model):
    idTeam = db.StringProperty(required=True)
    name = db.StringProperty(required=True)

class Game(db.Model):
    idTeam1 = db.StringProperty(required=True)
    idTeam2 = db.StringProperty(required=True)
    date = db.DateTimeProperty(required=False)
    goalsTeam1 = db.IntegerProperty()
    goalsTeam2 = db.IntegerProperty()
 
class User(db.Model):
    idUser = db.StringProperty(required=True)
    name = db.StringProperty(required=True)

