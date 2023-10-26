from os import walk, path

ejemplo_dir = input("Digite el directorio: ")
palabra = input("Digite la palabra que desea buscar en los archivos: ").lower()
dir_o_file = int(input("""\n¿Que quiere buscar?:

    1. Archivo
    2. Carpeta
            
    Elige un número:"""))

print("")

for nombre_directorio, directorios, ficheros in walk(ejemplo_dir):

    if dir_o_file == 1:
        for nombre_fichero in ficheros:
            if nombre_fichero.lower().count(palabra):
                print("Directorio: ", nombre_directorio)
                print(f"Archivo: {nombre_fichero}\n")

    if dir_o_file == 2:
        for directorio in directorios:
            if directorio.count(palabra):
                print(f"{path.join(nombre_directorio, directorio)}\n")