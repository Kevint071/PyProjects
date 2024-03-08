# Programa para calcular la cantidad de varillas posibles en un lugar (Tipo reja de una casa)

distancia = float(input("Digite la distancia donde irán las varillas en cm: "))
ancho_varillas = float(input("Digite el grosor de las varillas en cm: "))
espacio_varillas = float(input("Digite el espacio entre cada varilla en cm: "))

distancia_restante = distancia
num_varillas = 0
num_espacios = 0

# Aqui se determina la cantidad de varillas y espacios 

while distancia_restante > espacio_varillas:
    distancia_restante -= espacio_varillas
    num_espacios += 1

    if distancia_restante >= ancho_varillas + espacio_varillas:
        distancia_restante -= ancho_varillas

        num_varillas += 1
    else:
        break

print(f"\nLa cantidad de varillas que se pueden poner en este espacio es de {num_varillas:g} varillas")
print(f"La cantidad de espacios que hay en esta distancia es de {num_espacios:g}")
print(f"El espacio sobrante es de {distancia_restante:g} cm")

# Distribucion del espacio sobrante en los espacios de cada varilla

quitar_espacio = int(input("""\n\n¿Quieres quitar el espacio sobrante y distribuirlo en los espacio?

1. Sí 
2. No

: """))

if quitar_espacio == 1:
    espacio_varillas += (distancia_restante / num_espacios)
    print(f"\nPara que el espacio sobrante sea de 0, el espacio entre cada varilla debe ser de {espacio_varillas:g} cm")
