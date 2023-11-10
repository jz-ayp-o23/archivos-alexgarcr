with open('data/calificaciones.txt', 'r') as f_in:
    with open('data/promedios.txt', 'w') as f_out:
        for linea in f_in:
            palabras = linea.strip().split()
            nombres = palabras[0]
            apellidos = palabras[1]
            calificaciones = [int(calificacion) for calificacion in palabras[2:]]
            promedio = sum(calificaciones) / len(calificaciones)
            final = f'{apellidos.upper()}, {nombres}: {promedio:.1f}\n'
            f_out.write(final)