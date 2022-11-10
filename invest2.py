#Imprimir el total dels diners acumulats després de 7 anys utilitzant variables 
#Defino la funcion
def invest():
    #Declaramos las variables que necesitamos
    #dinero inicial
    savings = 100
    #valor a augmentar cada any
    increase = savings * 1.1
    años = 7
    a = 1
    resultado = 0
    #Declaramos un bucle while para mientras a sea mas grande o igual que los años haga estos calculos
    while a <= años:
        resultado += increase
        a += 1
    return resultado
#Guardamos el resultado en la variable "resultado" y llamamos a la funcion anterior
result = invest()
#Imprimimos por consola la variable resultado
print("Los ultimos 7 años has ahorrado un total de " + str(result) + "€")