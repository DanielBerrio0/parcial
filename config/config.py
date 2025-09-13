import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "db", "futbol_local.db")

SQLITE_URI = f"sqlite:///{DB_PATH}"

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_URI", SQLITE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
