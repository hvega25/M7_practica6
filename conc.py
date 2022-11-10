def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    # Actividad4

    # Variables

    x = 3
    y = 4
    name = "leo"
    name2 = "steven"

    # Prints

    print(x + y)
    print(name + " " + name2)
    print(f"La suma de x e y es: " + str(x + y))

    # Actividad 6


def actividad6(valor1, valor2):
    print(f'Hi, {actividad6(valor1, valor2)}')


if __name__ == '__main__':
    # Demanda de valores

    valor1 = int(input('Coloca un numero: '))
    valor2 = int(input('Coloca otro numero: '))

    # Suma de valores
    suma = valor1 + valor2

    # Print
    print(f"La suma del valor '{valor1}' mas el valor '{valor2}' es: " + str(suma))
