# Cómo usar este programa con una base de datos para aprender vocabulario de inglés</h1>

## 1. Crea una cuenta en fl0

Crea una cuenta gratuita en fl0 para obtener acceso a una base de datos PostgreSQL hosted.

## 2. Crea una base de datos

Una vez tengas acceso a fl0.com, crea una base de datos con el nombre **palabras**


## 3. Crea un archivo .env

Crea un archivo llamado .env en la carpeta Programa_aprender_ingles con los datos de conexión a tu base de datos:

    DATABASE_URL = "postgres://fl0user:cGbsEdO3mL9u@ep-little-violet-60084371.ap-southeast-1.aws.neon.tech:5432/palabras?sslmode=require"

Obten ese enlace en la pagina de fl0 el apartado de **Conection Info**

  - **postgres://** - Indica que es una conexión a PostgreSQL
  - **fl0user** - El usuario para la autenticación
  - **cGbsEdO3mL9u** - La contraseña del usuario fl0user
  - **ep-little-violet-60084371.ap-southeast-1.aws.neon.tech** - El host o dirección del servidor de base de datos  
  - **5432** - El puerto por defecto de PostgreSQL
  - **palabras** - El nombre de la base de datos específica a la que nos conectamos
  - **?sslmode=require** - Parámetro para forzar que la conexión use SSL

## 4. Ejecuta el programa

Finalmente, ejecuta el programa Aprender_palabras.py para interactuar con la base de datos. Podrás agregar palabras nuevas, estudiar las existentes, y más.

¡Y eso es todo! Sigue estos pasos para configurar una base de datos PostgreSQL para aprender vocabulario en inglés con este programa.
