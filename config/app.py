from flask import Flask, jsonify, request, abort

app = Flask(__name__)



# Obtener todos los grupos
@app.route('/futbol', methods=['GET'])
def get_futbol():
    return jsonify(rock_bands), 200

# Obtener un grupo por ID
@app.route('/futbol/<int:pais_id>', methods=['GET'])
def get_pais(pais_id):
    pais = db_session.query(Paises).filter_by(id=pais_id).first()
    if not pais:
        return jsonify({'error': 'La selección no se encontró'}), 404

    return jsonify({
        'id': pais.id,
        'nombre_pais': pais.nombre_pais
    }), 200


# Crear un nuevo grupo
@app.route('/futbol', methods=['POST'])
def create_pais():
    data = request.json
    if not data or 'nombre_pais' not in data:
        return jsonify({'error': 'Bad request, falta nombre_pais'}), 400
    
    nuevo_pais = Paises(nombre_pais=data['nombre_pais'])
    db_session.add(nuevo_pais)
    db_session.commit()
    
    return jsonify({
        'id': nuevo_pais.id,
        'nombre_pais': nuevo_pais.nombre_pais
    }), 201



# Actualizar un grupo existente
@app.route('/futbol/<int:pais_id>', methods=['PUT'])
def update_pais(pais_id):
    pais = db_session.query(Paises).filter_by(id=pais_id).first()
    if pais is None:
        return jsonify({'error': 'País no encontrado'}), 404
    
    data = request.json
    if not data:
        return jsonify({'error': 'Bad request'}), 400
    
    # Actualizamos solo el nombre_pais si está en el JSON
    if 'nombre_pais' in data:
        pais.nombre_pais = data['nombre_pais']
    
    db_session.commit()
    
    return jsonify({
        'id': pais.id,
        'nombre_pais': pais.nombre_pais
    }), 200


# Eliminar un grupo
@app.route('/futbol/<int:pais_id>', methods=['DELETE'])
def delete_pais(pais_id):
    pais = db_session.query(Paises).filter_by(id=pais_id).first()
    if pais is None:
        return jsonify({'error': 'País no encontrado'}), 404
    
    db_session.delete(pais)
    db_session.commit()
    
    return jsonify({'result': 'País eliminado'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
