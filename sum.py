#Imprimir la suma de 3 i 7 
#Funcion para sumar 3 + 7
#Defino la funcion para pasarle dos valores y que se sumen
def sumar(val1, val2):
    return val1 + val2
#Defino las variables que pasaremos para sumar
a = 3
b = 7
#Guardamos el resultado en la variable "resultado" y llamamos a la funcion anterior
resultado = sumar(a,b)
#Imprimimos por consola la variable resultado
print("La suma de los numeros " + str(a) + " i " + str(b) + " es " + str(resultado))