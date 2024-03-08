from datetime import datetime
import requests


def obtener_datos():
  url = "https://my.api.mockaroo.com/date_of_persons.json?key=251e0580"
  response = requests.get(url)

  if response.status_code == 200:
    datos_json = response.json()
    return datos_json
  else:
    print("Error al obtener los datos")
    return None


def calcular_edad_años(fecha_actual, fecha_nacimiento):
  años = fecha_actual.year - fecha_nacimiento.year

  if fecha_actual < datetime(fecha_actual.year, fecha_nacimiento.month, fecha_nacimiento.day).date():
    años -= 1

  return años


def run():
  datos = obtener_datos()
  datos_fecha_nacimiento = [datetime(*reversed(tuple(map(lambda x: int(x), persona["birthday"].split("/"))))).date() for persona in datos]

  fecha_actual = datetime.today().date()

  for indice, fecha_nacimiento in enumerate(datos_fecha_nacimiento):
    años = calcular_edad_años(fecha_actual, fecha_nacimiento)
    print(f"{indice+1}. {datos[indice]['first_name']} {datos[indice]['last_name']}: {años} años")


if __name__ == "__main__":
  run()