# Python, Flask, y SQLite

## Proyecto

El siguiente es un modelo básico de un sitio utilizando Python, Flask y Bootstrap.<br>
Además, el sitio muestra un blog que está almacenado en una base de datos SQLite. 

### Instalaciones previas

- Verificar instalación de pip mediante el comando:

      pip --version

- Si no está instalado, instalar pip mediante el comando:

      sudo apt install python3-pip

- Instalamos Flask mediante el comando: 

      pip install flask

> Nota: En PyCharm, esto lo podemos realizar desde Python Packages

### Creación del Proyecto

#### Archivo python: index.py

- crear index.py
- editar index.py
  - crear las rutas y las funciones

> Nota: El archivo init_db.py sirve para crear la base de datos `database.db` según la estructura declarada en `schema.sql` y luego agregar unos registros. 

#### Archivos HTML

Los archivos .html deben estar localizados en el directorio `/templates`

- Creación de un layout.html
  - agregar el contenido html reutilizable
  - luego colocar

        {% block content %}
        {% endblock %}

- En los archivos .html incluir layout.html mediante

      {% extends "layout.html" %}

- Luego incluir el código html que deseamos dentro del los siguientes comandos:

      {% block content %} 
      {% endblock %}

#### Archivos CSS

Los archivos .css debemos localizarlos en el directorio `/static/css`

#### Archivos SQLite

Los archivos de base de datos SQLite debemos colocarlos en el directorio `/src`
