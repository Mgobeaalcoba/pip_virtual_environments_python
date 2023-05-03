## Comandos para instalar Python en WSL o Ubuntu

```bash
sudo apt install python3 python3-pip
```
### Luego instalamos dependencias para el desarrollo en Python: 

```bash
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

### Con python3 y pip3 instalado ya podemos instalar las dependencias que queramos. Ejemplo: 

```bash
pip3 install matplotlib
```

### Luego podemos visualizar las dependencias que tenemos instaladas en nuestro proyecto así: 

```bash
pip3 freeze
```

Nos va a mostrar algo así: 

```
contourpy==1.0.7
cycler==0.11.0
fonttools==4.39.3
kiwisolver==1.4.4
matplotlib==3.7.1
numpy==1.24.3
packaging==23.1
pckGobea==0.1
Pillow==9.5.0
pyparsing==3.0.9
python-dateutil==2.8.2
six==1.16.0
```
Con esto vemos que cosas tenemos instalados en el entorno global de nuestra computadora. No en el entorno virtual de nuestro proyecto en particular. 

Instalar en el ambiente global de mi maquina no es una buena practica. Dado que para distintos proyectos puedo necesitar distintas versiones de una misma librería. Para esto se crearon **los ambientes virtuales en Python**. Encapsulan las librerías que necesito solo para ese proyecto. En otro proyecto puedo usar otras librerías u otras versiones de la misma librería. 

## Ambientes virtuales: 

1- ¿Verificar desde donde se está ejecutando python3? 

```bash
which python3
```

En mi caso: 

```
/c/Users/mgobea/AppData/Local/Microsoft/WindowsApps/python3
```

Lo mismo podría hacerse con pip3

```bash
which pip3
```
en mi caso

```
/c/Users/mgobea/AppData/Local/Microsoft/WindowsApps/pip3
```

Esto vaa cambiar cuando creemos nuestros ambientes virtuales...

2- Instalar python3-venv.

En WSL se hace así:

```bash
sudo apt install -y python3-venv
```

Creo que también se puede instalar con pip3 así: 

```bash
pip install python3-venv
```

Esta ultima forma puede servir para OS Windows con cmd.exe en lugar de WSL.

En general python3 ya viene con venv incluido por lo que no es necesario instalarlo. Se puede verificar ejecutando: 

```bash
python -m venv
```

Si nos pide un argumento adicional es porque efectivamente tenemos venv instalado en nuestro OS. 

3- Luego vamos a crear dentro de nuestro proyecto, una carpeta para nuestro ambiente virtual. Allí se almacenaran todas las librerías que descarguemos en ese **venv**

```bash
python3 -m venv my-env
```
Esto va a generar una carpeta dentro de la ubicación que le hayamos dado en el proyecto. En este caso se llama my-env y está dentro de la carpeta "app"

4- El proximo paso es activar nuestro ambiente recientemente creado para allí se ubiquen todas nuestras librerías descargadas y no en el ambiente global como veniamos haciendo hasta acá. Esto lo hacemos así: 

En Linux o WSL es:

```bash
source my-env/bin/activate
```

En Windows Nativo o Windows con cmd.exe es: 

```bash
.\my-env\Scripts\activate
```

Esto me va a colocar al costado de mi linea para ejecutar scripts en consola el nombre de mi environment entre parentesis. Eso significa que la activación fue exitosa. 

5- Para desactivar nuestro ambiente virtual entonces hacemos: 

```bash
deactivate
```
Eso quitará el nombre de nuestro environment del costado de nuestra linea para escribir scripts en consola. 

6- Finalmente si queremos guardar cualquier comando de consola en un alias, podemos hacerlo usando alias= en este caso vamos a guardar el comando de activación de los environments en "avenv" que es como normalmente se llama a este comando en el universo pythonico!!! 

```bash
alias avenv=.\my-env\Scripts\activate
```

Entonces ahora al ejecutar avenv en nuestra consola vamos a activar el environment y con deactivate lo desactivamos... Genial, no? 

Veamos entonces desde donde se ejecuta el environment y python3 con el ambiente encendido: 

```bash
which pip3
```
en mi caso

```
/c/Users/mgobea/Documents/develop/Python/pip_virtual_environments_python/app/my-env/Scripts/pip3
```
Si verificamos ahora con pip freeze los paquetes o librerías instalados vemos que no tenemos ninguno. 

--------------------------

### ¿Como gestionamos nuestras dependencias en Python? 

Con un archivo que tenemos que armar, ahora vemos el paso a paso y va en nuestro proyecto, se llama requirements.txt. El mismo contendrá todas las dependencias que el proyecto necesita poder ejecutarse con exito. 

1- Para guardar nuestras dependencias en el archivo mencionado hacemos: 

```bash
pip freeze > requirements.txt
```

2- Luego al descargar un archivo con requerimientos que esta dentro de un proyecto creamos un entorno virtual primero y luego hacemos:

```bash
pip install -r requirements.txt
```

-------------------------------

### Vamos a usar Docker para dockerizar nuestras aplicaciones. 

Vamos a dockerizar 2 tipos de aplicaciones:

1- La primera en la cual solo corres scripts

2- La segunda en donde necesitas el servidor web encendido y respondiendo peticiones. 

Vamos con la 1 que lo vamos a hacer con el proyecto "app":

1- Creo dentro del package un archivo "Dockerfile"

Un posible contenido es: 

```docker
# Declaro la versión de python que voy a usar en el proyecto:
FROM python:3.8

# Creo una carpeta raiz para el espacio de trabajo
WORKDIR /app
# Le indico cque me genere el archivo requirements.txt dentro de la carpeta raiz
COPY requirements.txt /app/requirements.txt

# Le digo que directamente me instale las dependencias que están en requirementes
# que no instale desde el cahce y que actualice lo que tenga que actualizar. 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiamos todo nuestro espacio de trabajo a la carpeta raiz
COPY . /app/

# Agrego un comando que va a mantener en ejecución constante nuestro contenedor:
CMD bash -c "while true; do sleep 1; done"
```

2- Creo un nuevo archivo llamado docker-compose.yml:

```docker
# Este archivo va a declarar como y desde donde se va a iniciar
# este contenedor

services:
  app-csv:
    build: 
      context: .
      dockerfile: Dockerfile
    

# Se lee como: "Vas a construir este servicio desde la carpeta
# en la que estoy ubicado y en esa carpeta que estás ubicado vas
# a buscar el archivo Dockerfile"
```

3- Para construir el contenedor que acabamos de programar debemos correr en consola el siguiente comando: 

```bash
docker-compose build
```

Si falla es porque docker no está encendido. En ese caso verificamos yendo al programa docker y viendo en la opcion de contenedores si está encendido o no lo está. 

Para que el comando funcione necesariamente deben estar creados los dos archivos mencionados en el punto 1 y 2 y debemos estar ubicados en la carpeta padre desde donde corremos esos archivos. 

4- Una vez construido el contenedor debemos lanzar el mismo con el siguiente comando: 

```bash
docker-compose up -d
```

5- Para ver el estado en el que se encuentra cada contenedor corremos:

```bash
docker-compose ps
```

6- Ya tenemos un contenedor que hemos generado con Python 3.8 pero ¿Como ingresamos a el? ¿Como trabajamos con el?

ejecutamos en bash: 

```bash
docker-compose exec app-csv bash
```

app-csv es el nombre de nuestro docker en el proyecto app. Cuando cambie el nombre debemos cambiar entonces la ultima parte del script de arriba. Esto nos va a abrir una terminal de tipo de bash en la cual estaremos trabajando bajo las condiciones y tecnologias descriptas en nuestro Dockerfile. 

De esta forma ya estaremos corriendo nuestro codigo en un ambiente de un contenedor de docker. 

7- Finalmente para salir del contenedor debemos escribir la palabra exit y dar enter. 

8- Salir no significa que nuestro contenedor deje de correr. Sino solo que hemos salido y no podemos operar sobre ella. Sigue "estando al aire". Para bajar nuestro contenedor debemos hacer: 

```bash
docker-compose down
```

9- Para volver a levantar nuestro contenedor de vuelta:

```bash
docker-compose up -d
```

10- Para conocer la version de Docker que estamos usando: 

```bash
docker-compose version
```

**¿Por que es tan importante Docker y armar contenedores? Porque puede usar mi contenedor otra persona que no necesita por ejemplo tener Python instalado en su computadora. Usando nuestro contenedor va a encontrarse con todo lo que necesita en su entorno de trabajo.**

Los contenedores de docker se pueden compartir y esa es su funcionalidad principal. Si bien como python developer vamos a usar mas los entornos virtuales de pip también nos vamos a cruzar con contenedores para trabajar con python o con otros lenguajes de programación con los que tengamos que interactuar. 

------------------------------------------------

Truco para enlazar los archivos sobre los que estoy desarrollando con los que están en el contenedor. De esa forma si modifico mis archivos también los voy a modificar en el contenedor. 


Ejemplo: Estoy dentro de mi contenedor y quiero cambiar el nombre que va a tener mi grafica de pie. 

1- Si lo actualizo en mi VSC o mi IDE directamente y guardo mis cambios no van a quedar guardados directamente en mi contenedor 

2- Esto es porque no están enlazados. Si quiesieramos mandar los cambios al contenedor deberiamos volver a comenzar todo el proceso descrito arriba desde el build hasta el up. 

3- Esto puede dañar la experiencia de desarrollo. Por lo que vamos a enlazarlos para que los cambios se suban solos...

4- En nuestro docker-compose vamos a agregar unas pocas palabras...

```docker
services:
  app-csv:
    build: 
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
```
La novedad acá en volumes y lo que sigue debajo que enlaza con la carpeta "app" es decir la carpeta padre que está dentro del contenedor. 

5- Para recrear la novedad en el docker-compose no debo volver a hacer build sino que alcanza con hacer nuevamente el up -d

----------------------------------------

**Lo mas común es dockerizar servidores web. Dado que al dockerizarlos va a ser mucho mas facil desplegar ese servidor en la nube.** 








