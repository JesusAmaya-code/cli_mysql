# Consulta de productos con Python y MySQL/MariaDB

Aplicacion escolar de linea de comandos que se conecta a MySQL o MariaDB,
ejecuta `SELECT * FROM productos` y muestra el resultado en una tabla.

## Requisitos

- Python 3 instalado.
- MySQL o MariaDB instalado y en ejecucion.
- Visual Studio Code.

## 1. Comprobar que el servidor funciona

En Windows, abre la terminal de VS Code con **Terminal > New Terminal**. Para
consultar el estado del servicio, ejecuta PowerShell:

```powershell
Get-Service -Name MySQL*,MariaDB* -ErrorAction SilentlyContinue
```

El valor de `Status` debe ser `Running`. El nombre exacto puede ser `MySQL80`,
`MySQL`, `MariaDB` u otro, segun la instalacion. Tambien puedes intentar una
conexion (el comando pedira la contraseña):

```powershell
mysql -h localhost -P 3306 -u root -p
```

Si el cliente muestra el prompt `mysql>`, el servidor acepta conexiones. Para
salir, escribe `exit`.

## 2. Crear la base de datos de ejemplo

Desde la carpeta del proyecto, importa el script. Sustituye `root` si utilizas
otro usuario:

```powershell
mysql -h localhost -P 3306 -u root -p < productos.sql
```

Si PowerShell no admite la redireccion con `<`, usa este comando:

```powershell
Get-Content .\productos.sql | mysql -h localhost -P 3306 -u root -p
```

El script crea la base de datos `tienda_escolar`, la tabla `productos` y cinco
registros de prueba. Conviene ejecutarlo una sola vez para no duplicar esos
registros.

## 3. Crear el entorno e instalar la dependencia

Ejecuta estos comandos exactos en la terminal PowerShell de VS Code:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell bloquea temporalmente la activacion, ejecuta primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 4. Configurar la conexion

El archivo `.env.example` solo documenta las variables necesarias. El programa
lee variables de entorno del sistema y no carga contraseñas desde el codigo.
Configuralas en la terminal actual, cambiando usuario y contraseña por los
datos de tu servidor:

```powershell
$env:DB_HOST="localhost"
$env:DB_HOST="localhost"
$env:DB_PASSWORD="TU_CONTRASEÑA"
$env:DB_PORT="3306"
$env:DB_NAME="tienda_escolar"
```

Estas variables duran solamente durante la sesion actual de la terminal. No
guardes una contraseña real en `.env.example` ni en Git.

## 5. Ejecutar el programa

En la misma terminal donde configuraste las variables, ejecuta:

```powershell
python .\testmysql.py
```

El programa mostrara los nombres de las columnas y todos los registros. Si no
hay registros, indicara que la tabla esta vacia. Si falla la conexion o la
consulta, mostrara un mensaje de error.


## Funcionamiento del codigo

`testmysql.py` obtiene host, usuario, contraseña, puerto y base de datos con
`os.getenv`. Luego `mysql.connector.connect` abre la conexion, el cursor ejecuta
unicamente `SELECT * FROM productos` y `fetchall` recupera los registros. Los
nombres se obtienen de `cursor.description` y los anchos se calculan para crear
una tabla legible. El bloque `except` informa errores y el bloque `finally`
cierra el cursor y la conexion.
