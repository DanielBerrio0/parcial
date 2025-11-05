from flask import Flask, render_template
from flask_jwt_extended import JWTManager  # <--- IMPORTANTE
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

    # --- Frontend Routes ---
    @app.route('/')
    def home():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
