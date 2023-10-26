from tkinter import filedialog, Tk


def obtener_directorio():
  root = Tk()
  root.withdraw()

  folder_path = filedialog.askdirectory()
  root.destroy()

  if not folder_path:
    print("Se canceló la selección del directorio...\n")
    return None
  return folder_path
