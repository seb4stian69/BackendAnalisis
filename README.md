# Backend para el proyecto final de analisis de tecnicas numericas
- Este repositorio tiene como finalidad mantener un sgv para el backend del proyecto final de analisis de tecnicas numericas

## Paso a paso para ejecutar
Luego de clonar el repositorio en el dispositivo, para poder ejecutar el servidor local de django se necesitan seguir los siguientes pasos

1. Instalar python en su version lts [aqui un <a href="https://www.python.org/downloads/">enlace</a>]
2. Despues de tener instalado python ir al directorio donde se clono el repositorio y ejecutar el siguiente comando <code>python -m venv venv</code> esto para crear el entorno virtual necesario para ejecutar django
3. Luego se debe activar ese entorno virtual usando el siguiente script que se encuentra en la carpeta venv generada anteriormente, para ello usar el siguiente ruta en el cmd <code>./venv/Scripts/activate</code>
4. Luego de ello instalar las librerias necesarias para ejecutar el proyecto <br>
<code>-1 pip install django</code> <br>
<code>-2 pip install numpy</code> <br>
<code>-3 pip pip install django-cors-headers</code>
5. Luego de eso ejecutar el servidor de django usando el siguiente comando <code>python manage.py runserver</code>

## Observacion #1
- En dado caso de que pida upgradear la version del pip ejecutar el siguiente comando <code>python.exe -m pip install --upgrade pip</code> y luego de que termine de actualizar la version volver a instalar la libreria que se intento instalar
