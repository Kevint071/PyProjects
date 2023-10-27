from math import pi, acos, degrees, tan


def obtener_datos():
    print("\n\n"+ "  PARA MEDIDAS PRECISAS DIGITE MEDIDA MÉTRICA  ".center(80, "-") + "\n\n")

    nombre_medidas = ["Milímetros", "Centímetros", "Decímetros", "Metros", "Decámetros", "Hectómetros", "Kilómetros"]
    medidas = ["mm", "cm", "dm", "m", "Dm", "Hm", "Km"]
    cantidad_medidas = list(range(1, len(medidas)+1))

    print("Medidas\n")

    while True:

        for item, nombre, medida in zip(cantidad_medidas, nombre_medidas, medidas):
            print(f"{item}. {nombre} ({medida})")

        medida = input("\nDigite una medida de la siguiente lista: ")

        if medida in medidas:
            print(f'\nNOTA: Se le asignara la medida "{medida}" a los datos que el usuario digite \n')
            break
        else:
            print("\nMedida no válida, digite la medida abreviada, Ej: cm, m, Dm\n")

    lista_datos = []

    radio = float(input("Digite el radio de la base circular del cilindro: "))
    largo = float(input("Digite el largo de el cilindro acostado: "))
    altura_agua = float(input("Digite la altura del agua con el cilindro acostado: "))

    lista_datos.append(radio)
    lista_datos.append(largo)
    lista_datos.append(altura_agua)

    return lista_datos, medida


def mostrar_datos(*datos):

    radio, largo, altura_agua, area, volumen, grados, area_radio_fondo, base_triangulo, area_triangulo, medida = datos

    print("\n\n"+ "  DATOS  ".center(80, "-") + "\n")

    print(f"Largo: {largo} {medida}")
    print(f"Radio: {radio} {medida}")
    print(f"Altura del agua: {altura_agua} {medida}\n")
    print(f"Área de la base: {area} {medida}²")
    print(f"Volumen del cilindro: {volumen} {medida}³\n")
    print(f"Grados triángulo área: {grados}°")
    print(f"Area desde el centro hasta fondo con esquina de altura agua: {area_radio_fondo} {medida}³\n")
    print(f"Base del triángulo: {base_triangulo} {medida}")
    print(f"Área del triángulo: {abs(area_triangulo)} {medida}\n")
    print(f"Área del agua: {(area_radio_fondo - area_triangulo):g} {medida}²")
    print(f"Volumen del agua: {((area_radio_fondo - area_triangulo) * largo):.2f} {medida}³")


def aproximar_datos(*datos):

    datos_aproximados = []
    
    for i in datos:
        i = (f"{i:g}")

        if i.count(".") >= 1:
            i = float(i)
        else:
            i = int(i)
        
        datos_aproximados.append(i)
    
    return datos_aproximados


def run():
    (radio, largo, altura_agua), medida = obtener_datos()

    radio, largo, altura_agua = aproximar_datos(radio, largo, altura_agua)

    area = pi * radio ** 2
    area, = aproximar_datos(area)

    volumen = area * largo
    volumen, = aproximar_datos(volumen)

    coseno = (radio - altura_agua) / radio 
    radianes = acos(coseno)
    grados = 2 * degrees(radianes)
    grados, = aproximar_datos(grados)

    area_radio_fondo = (pi * (radio ** 2)) * (grados /360)
    area_radio_fondo, = aproximar_datos(area_radio_fondo)

    tangente = tan(((grados/2) * pi)/180)

    base_triangulo = tangente * (radio - altura_agua)
    base_triangulo, = aproximar_datos(base_triangulo)

    area_triangulo = base_triangulo * (radio - altura_agua)
    
    mostrar_datos(radio, largo, altura_agua, area, volumen, grados, area_radio_fondo, base_triangulo, area_triangulo, medida)
    
if __name__ == "__main__":
    run()
