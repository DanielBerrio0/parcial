# Api - parcial

Este proyecto implementa una API REST desarrollada en Flask para gestionar selecciones nacionales de fútbol y los mundiales que han ganado. La API permite crear, listar, actualizar y eliminar países, así como registrar los mundiales asociados a cada uno.

Adicionalmente, se incorporó un Frontend que consume la API para facilitar el registro, autenticación e inicio de sesión de usuarios. El flujo de uso recomendado consiste en registrar un usuario, iniciar sesión con las credenciales creadas y, una vez autenticado correctamente, acceder a un panel principal (dashboard) donde se muestra el mensaje “Sesión iniciada correctamente”. Desde este panel es posible cerrar sesión y volver a la página de registro o autenticación cuando sea necesario.

La base de datos utilizada es SQLite, ubicada en el archivo db/futbol_local.db, y la aplicación está estructurada bajo una arquitectura que separa controladores, repositorios y modelos para mantener una organización clara del código.

Librerías necesarias:

* flask
* flask_sqlalchemy
* python-dotenv

Observaciones sobre errores previos que impedían el correcto funcionamiento del proyecto:
Existencia de dos archivos .db utilizados simultáneamente como base de datos (uno en la carpeta db y otro en la raíz), lo que generaba inconsistencias.
Los métodos del repositorio no realizaban los commit() correspondientes, por lo que los cambios no se persistían en la base de datos.
Existía confusión debido a la coexistencia de los archivos futbol_local.db y futbol_local.sql, lo que dificultaba identificar cuál era la base de datos real utilizada por el proyecto.
