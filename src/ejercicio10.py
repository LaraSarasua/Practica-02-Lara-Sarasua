def calcular_puntajes(rounds):
    puntajes = {}
    rondas_ganadas = {}
    mejor_ronda = {}
    cantidad_rondas = len(rounds)

    for nombre in rounds[0]['scores']:
        puntajes[nombre] = 0
        rondas_ganadas[nombre] = 0
        mejor_ronda[nombre] = 0
        
    
    for i in range(len(rounds)):
        ronda = rounds[i]
        print(f"\nRonda {i + 1} - {ronda['theme']}:")

        ganador = ""

        max_puntos = -1
        for nombre in ronda['scores']:
            datos = ronda['scores'][nombre]

            total = datos['judge_1'] + datos['judge_2'] + datos['judge_3']

            puntajes[nombre] += total

            if total > mejor_ronda[nombre]:
                mejor_ronda[nombre] = total
            
            if  total > max_puntos:
                max_puntos = total
                ganador = nombre

        rondas_ganadas[ganador] += 1
        print(f"  Ganador de la ronda: {ganador} con {max_puntos} puntos")

        print("  Tabla de puntajes:")
        for nombre in puntajes:
            print(f"    {nombre}: {puntajes[nombre]} pts")

    print("\nResultados finales:")
    nombres = list(puntajes.keys())

    print("ANTES DE ORDENAR:", nombres)

    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if puntajes[nombres[j]] > puntajes[nombres[i]]:
                nombres[i], nombres[j] = nombres[j], nombres[i]

    print("DESPUÉS DE ORDENAR:", nombres)

    for nombre in nombres:
        promedio = puntajes[nombre] / cantidad_rondas
        print(f"{nombre} - Total: {puntajes[nombre]} | Rondas ganadas: {rondas_ganadas[nombre]} | Mejor ronda: {mejor_ronda[nombre]} | Promedio: {round(promedio,1)}")