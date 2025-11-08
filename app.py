from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
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
    
    # Habilitar CORS para permitir peticiones desde el frontend
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Cargar configuración general
    app.config.from_object(Config)
    
    # --- Base de datos ---
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # --- Configuración JWT ---
    # Si JWT_SECRET_KEY está vacío, ponemos un valor por defecto para evitar errores
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY or "superclave-ultra-secreta-12345"
    app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION or ["headers"]
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES or 3600
    app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME or "Authorization"
    app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE or "Bearer"

    # Inicializar el manejador JWT
    jwt = JWTManager(app)

    # --- Blueprints ---
    app.register_blueprint(futbol_bp, url_prefix="/futbol")
    app.register_blueprint(user_bp, url_prefix="/")

    # --- API Root ---
    @app.route('/')
    def home():
        return jsonify({
            "api": "Parcial Backend API",
            "author": "DanielBerrio0",
            "description": "API RESTful con Flask, SQLAlchemy, JWT y estructura modular para gestión de usuarios y fútbol.",
            "endpoints": {
                "GET /": "Información de la API",
                "GET /health": "Health check",
                "POST /login": "Login y obtención de JWT",
                "POST /registry": "Registro de usuario",
                "GET /users": "Listado de usuarios (requiere JWT)",
                "GET /users/<id>": "Obtener usuario por ID",
                "PUT /users/<id>": "Actualizar usuario",
                "DELETE /users/<id>": "Eliminar usuario",
                "GET /futbol": "Endpoints de gestión de fútbol"
            },
            "repository": "https://github.com/DanielBerrio0/parcial",
            "status": "OK"
        })
    
    @app.route('/health')
    def health():
        return jsonify({
            "status": "OK",
            "message": "API is running"
        })

    return app


# Crear instancia de la aplicación para Gunicorn
app = create_app()


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
