# config/config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Ahora el archivo está en la carpeta db
SQLITE_URI = 'sqlite:///db/futbol_local.db'

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_URI", SQLITE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
