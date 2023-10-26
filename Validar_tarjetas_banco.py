def verificar_tarjeta():
    tarjeta = input("Digita la tarjeta bancaria: ")
    tarjeta = tarjeta.replace(" ", "")

    if len(tarjeta) != 16:
        print ("La longitud de la tarjeta es incorrecta")
    else:
        numeros_pares = [int(tarjeta[x]) for x in range(len(tarjeta)-2, -1, -2)]
        numeros_impares = [int(tarjeta[x]) for x in range(len(tarjeta)-1, -1, -2)]
        numeros_pares_x2 = list(map(lambda x: x*2 if x * 2 < 10 else int(str(x*2)[0]) + int(str(x*2)[1]), numeros_pares))

        suma_numeros = sum([x + y for x, y in zip(numeros_pares_x2, numeros_impares)])
        
        if suma_numeros % 10 == 0:
            print("Esta tarjeta es válida")
        else:
            print("Esta tarjeta no es válida")

if __name__ == "__main__":
    verificar_tarjeta()