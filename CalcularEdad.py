from datetime import date 
  
def calcularEdad(cumpleaños): 
    days_in_year = 365.2425    
    edat = int((date.today() - cumpleaños).days / days_in_year) 
    return edat 
          
print(calcularEdad(date(2003, 11, 25)), "años") 
