#variable global
areas = ["cuina",7.88, "menjador", 13.0, "terrassa", 20.34 , "lavabo" , 6.55,
         "habitacio1", 7.98 , "habitacio2", 12, "rebedor", 4.23]

#Función
def problema5():
    global areas
    print("Segundo elemento: " + str(areas[1]))
    print("Último elemento: " + str(areas[-1]) )
    print("Área de terrassa: " + str(areas[5]))
    print("Imprimir del primero al tercero : " + str(areas[1:3]))
    print("Imprimir del tercero al último : " + str(areas[3:-1]))
    print("Imprimir el total del área de las 2 habitaciones : " + str(areas[9]+ areas[11]))
    areas[7] = 7
    print("Modifica área de lavabo : " + str(areas))
    areas.append("patio interior")
    areas.append(2.78)

    print("Inserta a las dos últimas posiciones el patio interior y su área : " + str(areas))


#Lllamada de función
problema5()
