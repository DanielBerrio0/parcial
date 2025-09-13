from flask import Flask
from controllers.futbol_controller import futbol_bp  # Importar el Blueprint

app = Flask(__name__)


app.register_blueprint(futbol_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
