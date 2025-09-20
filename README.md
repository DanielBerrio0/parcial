# Api - parcial

Este proyecto implementa una API REST en Flask para gestionar selecciones nacionales de fútbol y los mundiales que han ganado.
Permite crear, listar, actualizar y eliminar países, así como registrar mundiales asociados a cada país.

La base de datos se maneja con SQLite (archivo db/futbol_local.db) y la capa de acceso está organizada en controladores, repositorios y modelos.

Las librerias necesarias son las siguientes:
* flask
* flask_sqlalchemy
* python-dotenv

Observaciones de por que el codigo no funcionaba antes:
* estaba intentando tener dos archivos .db como la base de datos, uno dentro de una carpeta llamada db y el otro en la raiz del proyecto.
* El repository no tenia los commit necesarios para que se actualizaran los cambios.
* confusion al tambien tener un futbol_local.db y futbol_local.sql, gracias a esto generaba confusion sobre cual era la base de datos en la que se iba a basar todo.
