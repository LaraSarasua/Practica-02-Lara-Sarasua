def analizador_de_texto(texto):
    lineas = texto.split("\n")

    total_lineas = len(lineas)
    total_palabras = 0
    palabras_por_linea = []

    for linea in lineas:
        palabras = linea.split()
        cantidad = len(palabras)
        palabras_por_linea.append(cantidad)
        total_palabras += cantidad
        
    promedio = total_palabras / total_lineas

    lineas_superiores = []

    for i in range(total_lineas):
        if palabras_por_linea[i] > promedio:
            lineas_superiores.append((lineas[i], palabras_por_linea[i]))
        
    return total_lineas, total_palabras, promedio, lineas_superiores

