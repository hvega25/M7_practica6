#variable globales

# variable que aumenta cada iteración
contador = 0

# variable que almacena la cantidad de dinero
dinero = 100

#función que contiene el código
def problema2():
    global dinero
    global contador
    # bucle
    while contador < 8:
        dinero = dinero + (dinero * 1.1)
        contador += 1


problema2()

#imprime la cantidad
print(dinero)