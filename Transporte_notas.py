opcion_cancion = int(input("""Seleccione la canción a transportar:
                           
    1. Canción de ejemplo
    2. Agregar una canción
    
    Elija una opción (Ej: 1): """))

cancion_notas_ejemplo = """// INTRODUCCIÓN

// Sol sol# Re#
// sol#
// Do# do sol#
// Fa m
// Sol sol# sol agudo
// Do m
// Do# do sol#
// Do#


// ESTROFA

sol# do do do la# do# sol#
sol#                   do#
Viniste a mi casa

do# do# do do# do
                 sol#    
Me visitaste

do do do do# re# do do# sol#
                              do#
Disfruté tu presencia

sol# fa re# do do 
                 Fam
Me cautivaste

do sol# sol fa re# fa sol#
                                  do#
No quiero que te vayas

sol# fa re# do# do do do#
                                    la#m
Yo quiero que te quedes

la# la# do do# do do# do do# do# do# re# re#
                do#                                     re#
He preparado un aposento para ti


// CORO

re# fa fa
               do#
Mi amado

re# fa fa
               la#m
Mi amado

do# do# do do# re# do# do do la# la# sol# la# do la# 
                            sol#                                   re#
Yo soy La Sunamita que te dice: Vive aquí

(Bis)

INTRODUCCIÓN
ESTROFA
CORO x2

re# sol# sol fa
                   Do#
Uh oh oh oh

re# sol# sol sol
                   Re#
Uh oh oh oh

re# sol# sol fa
                   Fam
Uh oh oh oh

re# sol# sol sol
                   Dom
Uh oh oh oh

(Bis)

// NO IMPORTA TODO LO QUE CUESTE

fa re# fa re# fa re# fa sol sol# sol
Do#                                                Re#
No importa todo lo que cueste

sol fa sol fa sol sol# sol fa fa
                                                 Fam
Tu presencia vale mucho más

fa re# fa re# fa sol sol# sol
Solo quiero estar contigo

sol sol# sol sol# sol sol# sol fa fa
Dom                                      Do#
Una y otra, y otra, y otra vez

fa re3 fa re# fa re# fa sol sol# sol
                                              Do# Re#
No importa todo lo que cueste

sol fa sol fa sol sol# la# do fa
                                     Re#      Fam
Tu presencia vale mucho más

fa re# fa re# fa sol sol# sol
Solo quiero estar contigo

sol sol# sol sol# sol sol# sol fa fa
Dom                Dom             Do#
Una y otra, y otra, y otra vez

(Bis) x2

CORO x2
No importa todo lo que cueste x4

// EN TU APOSENTO RESUCITARE 

do do re# fa re# fa re# fa re# fa
                  Do# 
En tu aposento resucitaré

re# re# sol# sol sol sol sol# sol re#
                   Re#
En tu aposento me levantaré

do do re# fa re# fa re# fa re# fa
                  Fam 
En tu aposento resucitaré

re# re# sol# sol sol sol sol# sol re#
                   Dom
En tu aposento me levantaré

(Bis) x1.5

NO IMPORTA  TODO LO QUE CUESTE x1.5
CORO x3
NO IMPORTA TODO LO QUE CUESTE""".lower()
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


