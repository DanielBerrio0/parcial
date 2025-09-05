from flask import Flask, jsonify, request, abort

app = Flask(__name__)



# Obtener todos los grupos
@app.route('/futbol', methods=['GET'])
def get_bands():
    return jsonify(rock_bands), 200

# Obtener un grupo por ID
@app.route('/futbol/<int:futbol_id>', methods=['GET'])
def get_band(band_id):
    band = next((b for b in rock_bands if b['id'] == band_id), None)
    if band is None:
        return jsonify({'error': 'La seleccion no se encontro'}), 404
    return jsonify(band), 200

# Crear un nuevo grupo
@app.route('/futbol', methods=['POST'])
def create_band():
    if not request.json or 'name' not in request.json or 'albums' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    new_id = max(b['id'] for b in rock_bands) + 1 if rock_bands else 1
    band = {
        'id': new_id,
        'name': request.json['name'],
        'albums': request.json['albums']
    }
    rock_bands.append(band)
    return jsonify(band), 201

# Actualizar un grupo existente
@app.route('/futbol/<int:band_id>', methods=['PUT'])
def update_band(band_id):
    band = next((b for b in rock_bands if b['id'] == band_id), None)
    if band is None:
        return jsonify({'error': 'Band not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    band['name'] = request.json.get('name', band['name'])
    band['albums'] = request.json.get('albums', band['albums'])
    return jsonify(band), 200

# Eliminar un grupo
@app.route('/futbol/<int:band_id>', methods=['DELETE'])
def delete_band(band_id):
    band = next((b for b in rock_bands if b['id'] == band_id), None)
    if band is None:
        return jsonify({'error': 'Band not found'}), 404
    rock_bands.remove(band)
    return jsonify({'result': 'Band deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
