import re
import timeit

def limpiar_nombre_re(nombre):
    return re.sub(r'[\\/\*?:"<>|]', '', nombre)

def limpiar_nombre_replace(nombre):
    caracteres_prohibidos = r'[\\/\*?:"<>|]'
    for caracter in caracteres_prohibidos:
        nombre = nombre.replace(caracter, '')
    return nombre

# Generar un millón de nombres de archivos de prueba
nombres = ['Archivo???Raro[123].txt'] * 10000

# Medir el tiempo de ejecución
tiempo_replace = timeit.timeit(lambda: [limpiar_nombre_replace(nombre) for nombre in nombres], number=1)
tiempo_re = timeit.timeit(lambda: [limpiar_nombre_re(nombre) for nombre in nombres], number=1)

print(f"Tiempo de ejecución con replace(): {tiempo_replace:.6f} segundos")
print(f"Tiempo de ejecución con re.sub(): {tiempo_re:.6f} segundos")