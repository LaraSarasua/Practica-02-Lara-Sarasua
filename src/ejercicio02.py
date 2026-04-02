def calcular_duracion_total(playlist):
    duracion_total = 0

    for cancion in playlist:
        minutos, segundos = cancion["duration"].split(":")
        duracion_total += int(minutos) * 60 + int(segundos)
    minutos = duracion_total // 60
    segundos = duracion_total % 60

    return minutos, segundos

def calcular_min_and_max(playlist):
    canciones = []

    for cancion in playlist:
        minutos, segundos = cancion["duration"].split(":")
        duracion_total = int(minutos) * 60 + int(segundos)
        
        canciones.append({
            "title": cancion["title"],
            "segundos": duracion_total,
            "original": cancion["duration"]
        })

    duracion_minima = min(canciones, key=lambda x: x["segundos"])
    duracion_maxima = max(canciones, key=lambda x: x["segundos"])

    return duracion_minima, duracion_maxima