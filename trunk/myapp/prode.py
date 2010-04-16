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

class GameXP(db.Model):
    idGroup = db.StringProperty()
    matchNumber = db.IntegerProperty()
    date = db.DateTimeProperty()
    place = db.StringProperty()
    idTeam1 = db.StringProperty()
    idTeam2 = db.StringProperty()    
    nameTeam1 = db.StringProperty()
    nameTeam2 = db.StringProperty()    
    goalsTeam1 = db.IntegerProperty()
    goalsTeam2 = db.IntegerProperty()
    
#'A','1','11/06 16:00','Johannesburg - JSC','South Africa','South Africa','Mexico','Mexico'