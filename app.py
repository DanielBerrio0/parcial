from flask import Flask
from config.config import Config
from extensions import db
from controllers.futbol_controller import futbol_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)


    with app.app_context():
        db.create_all()


    app.register_blueprint(futbol_bp, url_prefix="/futbol")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
