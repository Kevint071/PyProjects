
def run():
  codificacion = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"

  valor = 0

  for i in codificacion:
    if i == "&":
      print(valor, end="")
    elif i == "#":
      valor += 1
    elif i == "@":
      valor -= 1
    elif i == "*":
      valor *= valor

if __name__ == "__main__":
  run()