from datetime import datetime


def obtener_datos(text_dato):
  datos_nacimiento = []
  for i in range(3):
    while True:
      try:
        dato = int(input(f"Digite el {text_dato[i]} de nacimiento: "))
        datos_nacimiento.append(dato)
        break
      except:
        print("Dato no válido...\n")

  return datos_nacimiento


def calcular_edad_años(fecha_actual, fecha_nacimiento):
  años = fecha_actual.year - fecha_nacimiento.year

  if fecha_actual < datetime(fecha_actual.year, fecha_nacimiento.month, fecha_nacimiento.day).date():
    años -= 1

  return años


def run():
  datos_fecha_nacimiento = obtener_datos(("dia", "número del mes", "año"))
  fecha_nacimiento = datetime(*reversed(datos_fecha_nacimiento)).date()
  fecha_actual = datetime.today().date()
  
  años = calcular_edad_años(fecha_actual, fecha_nacimiento)
  print(f"\nLa edad es de {años} años")



if __name__ == "__main__":
  run()