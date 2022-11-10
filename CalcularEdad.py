#Importo date de datetime, que es una clase creada ya de python
from datetime import date 
#declaro la funcion que le pasamos una fecha y te dice tu edad
def calcularEdad(cumpleaños):
    #declaro variables necessarias
    año = 365.2425    
    edat = int((date.today() - cumpleaños).days / año) 
    return edat
#Hacemos un print que te indicara tu edad
print("Usted tiene "+str(calcularEdad(date(2003, 11, 25))), "años") 
