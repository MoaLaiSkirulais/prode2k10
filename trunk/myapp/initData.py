import pprint
from google.appengine.ext import db
import sys; sys.path.append('myapp')
import prode

def init():

    pp = pprint.PrettyPrinter(indent=4)
    
    TEAMS= [
            ['ko', 'Corea del Sur'],
            ['ao', 'Ghana'],
            ['do', 'Nueva Zelanda'],
            ['4o', 'Argelia'],
            ['22', 'Costa de Marfil'],
            ['33', 'Grecia'],
            ['44', 'Holanda'],
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
    
    pp.pprint(TEAMS)
    
    for team in prode.Team.all():
        team.delete()
            
    for item in TEAMS:
        t1 = prode.Team(idTeam=item[0], name=item[1])
        t1.put()
    
    GAMES= [
            ['A','1','11/06 16:00','Johannesburg - JSC','South Africa','South Africa','Mexico','Mexico'], 
            ['A','2','11/06 20:30','Cape Town','Uruguay','Uruguay','France','France'], 
            ['A','17','16/06 20:30','Tshwane/Pretoria','South Africa','South Africa','Uruguay','Uruguay'], 
            ['A','18','17/06 20:30','Polokwane','France','France','Mexico','Mexico'], 
            ['A','33','22/06 16:00','Rustenburg','Mexico','Mexico','Uruguay','Uruguay'], 
            ['A','34','22/06 16:00','Mangaung / Bloemfontein','France','France','South Africa','South Africa'], 
            ['B','3','12/06 16:00','Johannesburg - JEP','Argentina','Argentina','Nigeria','Nigeria'], 
            ['B','4','12/06 13:30','Nelson Mandela Bay/Port Elizabeth','Korea Republic','Korea Republic','Greece','Greece'], 
            ['B','19','17/06 16:00','Mangaung / Bloemfontein','Greece','Greece','Nigeria','Nigeria'], 
            ['B','20','17/06 13:30','Johannesburg - JSC','Argentina','Argentina','Korea Republic','Korea Republic'], 
            ['B','35','22/06 20:30','Durban','Nigeria','Nigeria','Korea Republic','Korea Republic'], 
            ['B','36','22/06 20:30','Polokwane','Greece','Greece','Argentina','Argentina'], 
            ['C','5','12/06 20:30','Rustenburg','England','England','USA','USA'], 
            ['C','6','13/06 13:30','Polokwane','Algeria','Algeria','Slovenia','Slovenia'], 
            ['C','22','18/06 16:00','Johannesburg - JEP','Slovenia','Slovenia','USA','USA'], 
            ['C','23','18/06 20:30','Cape Town','England','England','Algeria','Algeria'], 
            ['C','37','23/06 16:00','Nelson Mandela Bay/Port Elizabeth','Slovenia','Slovenia','England','England'], 
            ['C','38','23/06 16:00','Tshwane/Pretoria','USA','USA','Algeria','Algeria'], 
            ['D','7','13/06 20:30','Durban','Germany','Germany','Australia','Australia'], 
            ['D','8','13/06 16:00','Tshwane/Pretoria','Serbia','Serbia','Ghana','Ghana'], 
            ['D','21','18/06 13:30','Nelson Mandela Bay/Port Elizabeth','Germany','Germany','Serbia','Serbia'], 
            ['D','24','19/06 16:00','Rustenburg','Ghana','Ghana','Australia','Australia'], 
            ['D','39','23/06 20:30','Johannesburg - JSC','Ghana','Ghana','Germany','Germany'], 
            ['D','40','23/06 20:30','Nelspruit','Australia','Australia','Serbia','Serbia'], 
            ['E','9','14/06 13:30','Johannesburg - JSC','Netherlands','Netherlands','Denmark','Denmark'], 
            ['E','10','14/06 16:00','Mangaung / Bloemfontein','Japan','Japan','Cameroon','Cameroon'], 
            ['E','25','19/06 13:30','Durban','Netherlands','Netherlands','Japan','Japan'], 
            ['E','26','19/06 20:30','Tshwane/Pretoria','Cameroon','Cameroon','Denmark','Denmark'], 
            ['E','43','24/06 20:30','Rustenburg','Denmark','Denmark','Japan','Japan'], 
            ['E','44','24/06 20:30','Cape Town','Cameroon','Cameroon','Netherlands','Netherlands'], 
            ['F','11','14/06 20:30','Cape Town','Italy','Italy','Paraguay','Paraguay'], 
            ['F','12','15/06 13:30','Rustenburg','New Zealand','New Zealand','Slovakia','Slovakia'], 
            ['F','27','20/06 13:30','Mangaung / Bloemfontein','Slovakia','Slovakia','Paraguay','Paraguay'], 
            ['F','28','20/06 16:00','Nelspruit','Italy','Italy','New Zealand','New Zealand'], 
            ['F','41','24/06 16:00','Johannesburg - JEP','Slovakia','Slovakia','Italy','Italy'], 
            ['F','42','24/06 16:00','Polokwane','Paraguay','Paraguay','New Zealand','New Zealand'], 
            ['G','13','15/06 16:00','Nelson Mandela Bay/Port Elizabeth','Cote dIvoire','Cote dIvoire','Portugal','Portugal'], 
            ['G','14','15/06 20:30','Johannesburg - JEP','Brazil','Brazil','Korea DPR','Korea DPR'], 
            ['G','29','20/06 20:30','Johannesburg - JSC','Brazil','Brazil','Cote dIvoire','Cote dIvoire'], 
            ['G','30','21/06 13:30','Cape Town','Portugal','Portugal','Korea DPR','Korea DPR'], 
            ['G','45','25/06 16:00','Durban','Portugal','Portugal','Brazil','Brazil'], 
            ['G','46','25/06 16:00','Nelspruit','Korea DPR','Korea DPR','Cote dIvoire','Cote dIvoire'], 
            ['H','15','16/06 13:30','Nelspruit','Honduras','Honduras','Chile','Chile'], 
            ['H','16','16/06 16:00','Durban','Spain','Spain','Switzerland','Switzerland'], 
            ['H','31','21/06 16:00','Nelson Mandela Bay/Port Elizabeth','Chile','Chile','Switzerland','Switzerland'], 
            ['H','32','21/06 20:30','Johannesburg - JEP','Spain','Spain','Honduras','Honduras'], 
            ['H','47','25/06 20:30','Tshwane/Pretoria','Chile','Chile','Spain','Spain'], 
            ['H','48','25/06 20:30','Mangaung / Bloemfontein','Switzerland','Switzerland','Honduras','Honduras'] 
        ] 
        
    pp.pprint(GAMES)
    pp.pprint("---")

    for item in GAMES:
        pp.pprint("-")
        pp.pprint(item)
        
#http://www.fifa.com/worldcup/matches/index.html