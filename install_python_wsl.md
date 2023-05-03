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