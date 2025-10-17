import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from extensions import db

logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno desde .env
load_dotenv()

MYSQL_URI = os.getenv('MYSQL_URI')
SQLITE_URI = 'sqlite:///bands_local.db'

# Configurar Flask y Flask-SQLAlchemy
app = Flask(__name__)

# Asignar la URI de la base de datos (ya sea MySQL o SQLite)
if MYSQL_URI:
    app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_URI

# Desactivar el seguimiento de modificaciones en objetos de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy con la app
db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    try:
        db.create_all()  # Esto crea las tablas en la base de datos si no existen
        logging.info('Las tablas han sido creadas exitosamente.')
    except Exception as e:
        logging.error(f'Error al crear las tablas: {e}')

# Función para obtener la sesión de la base de datos
def get_db_session():
    """
    Retorna una nueva sesión de base de datos para ser utilizada en los servicios o controladores.
    """
    return db.session
