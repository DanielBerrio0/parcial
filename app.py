from flask import Flask
from config.config import Config
from extensions import db  # Importa el objeto db desde extensions.py
from controllers.futbol_controller import futbol_bp
from controllers.users_controllers import user_bp
from config.jwt import JWT_ACCESS_TOKEN_EXPIRES, JWT_HEADER_NAME, JWT_HEADER_TYPE, JWT_SECRET_KEY, JWT_TOKEN_LOCATION


def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)

    # Cargar la configuración desde el objeto Config
    app.config.from_object(Config)

    # Inicializar la extensión db con la aplicación
    db.init_app(app)  # Asegúrate de que esta línea esté presente

    # Crear las tablas en la base de datos
    with app.app_context():
        db.create_all()

    # Registrar los blueprints
    app.register_blueprint(futbol_bp, url_prefix="/futbol")
    app.register_blueprint(user_bp, url_prefix="/")  # Cambia el prefijo si es necesario

    # Configurar JWT
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
    app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
    app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

    return app


# Crear la aplicación y ejecutar
if __name__ == "__main__":
    app = create_app()  # Llamar a create_app() para obtener la app configurada
    app.run(host="0.0.0.0", port=5000, debug=True)
