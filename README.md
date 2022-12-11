# Software
Aplicacion de escritorio encargada del manejo del sistema.

## Para comenazar

### 1) Crear un **virtual enviroment** de python con la version de python **3.7** : 

```
py -m virtualenv -p=<Ruta de instalacion de pyhon 3.7>Python37\python.exe QTvenv
```
### 2)  Activar el venv en windows :

En powershell probablemente se necesite dar permisos :
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
Luego ejecutar :
```
./QTvenv/Scripts/Activate.ps1
```
### 3) Instalar las dependencias necesarias : 
```
pip install -r requirements.txt
```
### 4) En windows se debe corregir una de las dependencias ejecutando

```
pipwin install cairocffi
```
### 5) Listo, ya se puede correr la aplicacion ```py main.py```
