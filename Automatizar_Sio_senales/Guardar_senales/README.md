# Guardar Señales

### Hay 2 cosas que hay a tomar en cuenta:

<br>

1. El archivo a ejecutar es **main.py** ya que este es el archivo principal. Los archivos **Cataloguer_guardar.py** y **Saver.py** son archivos que no se ejecutan directamente sino que ayudan a que **main.py** funcione correctamente.

<br>

2. Por defecto, el archivo **main.py** no abre una ventana de un navegador para ejecutarse ya que así funciona mucho mejor, pero si aun así quieren que mientras se ejecuta este archivo la ventana del navegador se muestre, tienen que importar este modulo en el archivo **Saver.py** para que la pantalla se muestre correctamente:

    <br>

        from screeninfo import get_monitors
    
    <br>
    
    Luego tienen que poner este codigo en el mismo archivo (**Saver.py**) para que renderize el tamaño de la pestaña que está en el navegador acorde al tamaño de su monitor. Este código se debe agregar en la linea 23 reemplazando el comentario "**Aqui va el codigo de renderizado de página que se explica en el README.md**" por este código:

    <br>

        monitor = get_monitors()[0]
        width = monitor.width
        height = monitor.height
        await page.setViewport({'width': width, 'height': height})
    
    <br>

    Ahora para que se muestre la ventana del navegador tienen que poner el siguiente codigo tambien en el archivo **Saver.py** en los parametros de la funcion **launch()**. Esta linea se encuentra en la linea 18 y tiene el siguiente código:

    <br>

        browser = await pyppeteer.launch()
    
    <br>

    Debe quedar así:

    <br>

        browser = await pyppeteer.launch(headless=False, args=['--start-maximized'])
    
    <br>

    Si quieren abrir la ventana con un navegador especifico deben poner el siguiente argumento y la direccion de ese navegador ejecutable:

        browser = await pyppeteer.launch(headless=False, executablePath=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", args=['--start-maximized'])
