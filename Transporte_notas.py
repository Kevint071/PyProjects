opcion_cancion = int(input("""Seleccione la canción a transportar:
                           
    1. Canción de ejemplo
    2. Agregar una canción
    
    Elija una opción (Ej: 1): """))

cancion_notas_ejemplo = """Ritmo de intro (re# la# sol,   do# la# fa,    do sol# fa)

Re# Re# Re# Re# do do# do la#
Lights go out and I can't be saved

Do#     do# do# do#     do# do la# sol#
Tides that I tried to swim against

Re# re# re# do do# do la#
Have brought me down upon my knees

Do#     do# do#     la# do la# sol fa re# 
Oh, I beg, I beg and plead, singing

Re# re# do do# do la#
Come out of things unsaid

Do#    do# do#     la# do la# sol# 
Shoot an apple off my head

Fa re# Re# re# do do# do la#
And a trouble that can't be named

La# do# do# do# la# do la# sol# fa re#
A tiger's waiting to be tamed, singing

(Sol sol# fa re# sol)x2
You are, you are

Re#x3 do# do la#
Confusion never stops

Do#x4 do la# sol# 
Closing walls and ticking clocks

Fa re# Re#x2 do do# do la#
Gonna come back and take you home

La# do#x3 la# do la# sol# fa re#
I could not stop that you now know, singing

Re#x2 do do# do la#
Come out upon my seas

Do#x3 la# do la# sol#
Cursed missed opportunities

Fa re# re#x2 do# do la#
Am I a part of the cure?

La# do#x3 la# do la# sol# fa re#
Or am I part of the disease? Singing

(Sol sol# fa re# sol)x2
You are, you are

(Sol sol# fa re# sol)x2
You are, you are

Ritmo de intro (re# la# sol,   do# la# fa,    do sol# fa)
You are, you are""".lower()
cancion_notas = cancion_notas_ejemplo if opcion_cancion == 1 else input("\nAgregue la cancion con las notas: ")


notas_mayores = {"do": 0, "do#": 1, "re": 2, "re#": 3, "mi": 4, "fa": 5, "fa#": 6, "sol": 7, "sol#": 8, "la": 9, "la#": 10, "si": 11}
notas_menores = {"dom": 0, "do#m": 1, "rem": 2, "re#m": 3, "mim": 4, "fam": 5, "fa#m": 6, "solm": 7, "sol#m": 8, "lam": 9, "la#m": 10, "sim": 11}

cancion_notas = cancion_notas.split("\n")
cancion_notas_palabras = list(map(lambda x: x.split(" "), cancion_notas))

subir_bajar_tono = int(input("""\nElija la dirección del transporte de notas: 

  1. Subir tono
  2. Bajar tono

  Elija una opción (Ej: 1): """))

palabra_tono = "subir" if subir_bajar_tono  == 1 else "bajar"
semitonos = int(input(f"\n¿Cuantos semitonos quiere {palabra_tono}? (Ej: 4): "))

indices_notas_mayores = {v: k for k, v in notas_mayores.items()}
indices_notas_menores = {v: k for k, v in notas_menores.items()}


for linea in cancion_notas_palabras:
  for i in range(len(linea)):
    palabra = linea[i]
    if palabra in notas_mayores:
      indice_nota = notas_mayores[palabra] + semitonos
      if indice_nota >= 12:
        indice_nota -= 12
      linea[i] = indices_notas_mayores[indice_nota]
    elif palabra in notas_menores:
      indice_nota = notas_menores[palabra] + semitonos
      if indice_nota >= 12:
        indice_nota -= 12
      linea[i] = indices_notas_menores[indice_nota]

cancion_transportada = []
     
for linea in cancion_notas_palabras:

  cancion_transportada.append(" ".join(linea).capitalize())

cancion_transportada = "\n".join(cancion_transportada)
print(cancion_transportada)


