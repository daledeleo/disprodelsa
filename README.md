# Sistema farmacoterapéutico Disprodelsa

_El presente proyecto tiene como objetivo llevar un control de la famacoterapia de un paciente_

## Comenzando 🚀

_Estas instrucciones detallas a continuación son las que se permitará levantar este aplicativo web de manera local._


### Pre-requisitos 📋

_Lo que necesita antes de empezar_


* Instalar [Python](https://www.python.org/) se recomienda python 3.8.7

* Instalar [Nodejs](https://nodejs.org/es/) se recomienda nodejs v14.15.1


### Instalación Backend Django de python 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

1. Crear un ambiente virtual en python y activarlo (esto es opcional) explicado en [link](https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace/)

2. Luego ubicarse en el directorio del proyecto e instalar el archivo requirements.txt
```
pip install requirements.txt
```
_Esto instalará todas las librerias necesarias para el backend_

3. Luego realizar las migraciones de los modelos a la base de datos
```
python manage.py migrate
```
_luego_
```
python manage.py makemigrations
```

_si esto falla entonces ejecutar_
```
python manage.py makemigrations core
```
_y luego_
```
python manage.py migrate
```


4. En este punto se tiene la base de datos ya desplejada en sq.lite3
_luego crear un superusuario_

```
python manage.py createsuperuser
```

_Proceder añadir un email y una contraseña esto es para enviar los correos electronicos_
_Esta contraseña se la recomienda obtener en luego de activar la verificacion de 2 pasos de gmail_
_EMAIL_HOST_USER=<example@.com>
EMAIL_HOST_PASSWORD=<<password>>_
_Finalmente dejar .env.example como .env_
5. Y finalmente levantar el servidor de django para el backend
 ```
 python manage.py runserver
 ```
6. Creacion de usuario administrador para el inicio de sesión en el frontend
_ir a localhost:8000 en los usuario del sistema crear un usario para comenzar el login el frontend_
_Se tiene que llenar todos los campos necesarios_

## Instalación del frontend🔧
_Este sera el encargado de actuar como intermediaria entre el usuario y la base de datos, mostrando las diversas pantallas de la aplicación_
1. Digirse dentro de la carpeta frontend
_y ejecutar lo siguiente_
```
npm install
```
_esto instalara todas las librerias necesarias para la ejecucion del aplicativo_

2. Iniciar el servidor frontend
```
npm start
```
_esto levantara el proyecto en el puerto 8080 http://localhost:8080_
_Por favor modificar las credenciales dentro de los modulos de Crear Cuenta y Restablecimiento de contraseña con las credenciales agregadas el momento de crear un superusuario o agregar las credenciales de un administrador del sistema_
