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










