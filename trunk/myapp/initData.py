from google.appengine.ext import db
import sys; sys.path.append('myapp')
import prode

def init():
        
    TEAMS= [
            ['ko', 'Corea del Sur'],
            ['ko', 'Ghana'],
            ['ko', 'Nueva Zelanda'],
            ['ko', 'Argelia'],
            ['ko', 'Costa de Marfil'],
            ['ko', 'Grecia'],
            ['ko', 'Holanda'],
            ['ko', 'Argentina'],
            ['ko', 'Dinamarca'],
            ['ko', 'Honduras'],
            ['ko', 'Paraguay'],
            ['ko', 'Australia'],
            ['ko', 'Eslovaquia'],
            ['ko', 'Inglaterra'],
            ['ko', 'Portugal'],
            ['ko', 'Brasil'],
            ['ko', 'Eslovenia'],
            ['ko', 'Italia'],
            ['ko', 'Serbia'],
            ['ko', 'Camerun'], 	
            ['ko', 'Espania'],
            ['ko', 'Japon'],
            ['ko', 'Sudafrica'],
            ['ko', 'Chile'],
            ['ko', 'Estados Unidos'],
            ['ko', 'Mexico'],
            ['ko', 'Suiza'],
            ['ko', 'Corea del Norte'],
            ['ko', 'Francia'],
            ['ko', 'Nigeria'],
            ['ko', 'Uruguay']
            ]
            
    for team in prode.Team.all():
        team.delete()
            
    for item in TEAMS:
        t1 = prode.Team(idTeam=item[0], name=item[1])
        t1.put()
