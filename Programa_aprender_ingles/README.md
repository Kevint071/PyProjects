<style>
  h1 {
    color: #e6490b;
  }
  h2 {
    color: #0077b5;
  }
  code {
    font-size: 14px;
    background-color: #222;
    margin-bottom: 0px;
    color: #ffffdd;
    padding: 2px 10px;
    border-radius: 4px;
  }
  p,
  ul,
  li {
    
    font-size: 16px;
  }
</style>

<h1>Cómo usar este programa con una base de datos para aprender vocabulario de inglés</h1>

<h2>1. Crea una cuenta en fl0</h2>
<p>Crea una cuenta gratuita en fl0 para obtener acceso a una base de datos PostgreSQL hosted.</p>

<h2>2. Crea una tabla</h2>
<p>Una vez tengas acceso a la base de datos, crea una tabla llamada palabras con los siguientes campos:</p>

<ul>
  <li>id: llave primaria autoincremental</li>
  <li>palabra: texto con la palabra en inglés</li>
  <li>traduccion: texto con la traducción al español</li>
</ul>

<p>Puedes crear la tabla ejecutando el siguiente SQL:</p>

<code>CREATE TABLE palabras (
id SERIAL PRIMARY KEY,
palabra TEXT,
traduccion TEXT
);</code>

<h2>3. Crea un archivo credenciales.py</h2>
<p>Crea un archivo llamado credenciales.py en la carpeta Programa_aprender_ingles con los datos de conexión a tu base de datos:</p>

<code>

<p>from psycopg2 import connect <br><br>
conn = connect("postgres://fl0user:cGbsEdO3mL9u@ep-little-violet-60084371.ap-southeast-1.aws.neon.tech:5432/palabras?sslmode=require")</p></code>

<p>Reemplaza usuario, contraseña, host, puerto y db con los valores correspondientes a tu base de datos.</p>
<ul>
    <li>
    <strong>postgres://</strong> - Indica que es una conexión a PostgreSQL
    </li>
    <li>
    <strong>fl0user</strong> - El usuario para la autenticación
    </li>
    <li>
    <strong>cGbsEdO3mL9u</strong> - La contraseña del usuario fl0user
    </li>
    <li>
    <strong>ep-little-violet-60084371.ap-southeast-1.aws.neon.tech</strong> - El host o dirección del servidor de base de datos  
    </li>
    <li>
    <strong>5432</strong> - El puerto por defecto de PostgreSQL
    </li>
    <li>
    <strong>palabras</strong> - El nombre de la base de datos específica a la que nos conectamos
    </li>
    <li>
    <strong>?sslmode=require</strong> - Parámetro para forzar que la conexión use SSL
    </li>
</ul>
<h2>4. Ejecuta el programa</h2>
<p>Finalmente, ejecuta el programa Aprender_palabras.py para interactuar con la base de datos. Podrás agregar palabras nuevas, estudiar las existentes, y más.</p>

<p>¡Y eso es todo! Sigue estos pasos para configurar una base de datos PostgreSQL para aprender vocabulario en inglés con este programa.</p>
