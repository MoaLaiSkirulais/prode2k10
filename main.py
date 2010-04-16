import pprint
import cgi
import imp
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import sys; sys.path.append('myapp')

import prode
import initData
  
class InitDb(webapp.RequestHandler):
    
    def get(self):
 
        #print dir(prode)
        #reload(initData)
        initData.init()
 
class Main(webapp.RequestHandler):

    def get(self):
        print dir(prode)
            
        t1 = prode.Team(idTeam="AR", name="Argentina",)
        t2 = prode.Team(idTeam="BR", name="Brasil",)
            
        g1=prode.Game(idTeam1="AR", idTeam2="BR")
        g1.put()	

#--    
application = webapp.WSGIApplication(
                                     [('/', Main),
                                     ('/initDb', InitDb)],
                                     debug=True)
                                     
def main():

    run_wsgi_app(application)

if __name__ == "__main__":
  main()
  