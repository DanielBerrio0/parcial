# app.py
from flask import Flask
from flask_jwt_extended import JWTManager   # <--- IMPORTANTE
from config.config import Config
from extensions import db
from controllers.futbol_controller import futbol_bp
from controllers.users_controllers import user_bp
from config.jwt import (
    JWT_ACCESS_TOKEN_EXPIRES,
    JWT_HEADER_NAME,
    JWT_HEADER_TYPE,
    JWT_SECRET_KEY,
    JWT_TOKEN_LOCATION
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Configurar JWT
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
    app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
    app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

    # 🔥 Inicializar el manejador JWT
    jwt = JWTManager(app)

    # Registrar blueprints
    app.register_blueprint(futbol_bp, url_prefix="/futbol")
    app.register_blueprint(user_bp, url_prefix="/")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
