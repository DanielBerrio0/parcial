from flask import Blueprint, jsonify, request
from repository.futbol_repository import PaisRepository
from config.database import get_db_session

futbol_bp = Blueprint('futbol_bp', __name__)
pais_repo = PaisRepository(db_session)

@futbol_bp.route('/futbol', methods=['GET'])
def get_paises():
    paises = pais_repo.get_all_paises()
    resultado = [{'id': p.id, 'nombre_pais': p.nombre_pais} for p in paises]
    return jsonify(resultado), 200

@futbol_bp.route('/futbol/<int:pais_id>', methods=['GET'])
def get_pais(pais_id):
    pais = pais_repo.get_pais_by_id(pais_id)
    if not pais:
        return jsonify({'error': 'La selección no se encontró'}), 404
    return jsonify({'id': pais.id, 'nombre_pais': pais.nombre_pais}), 200

@futbol_bp.route('/futbol', methods=['POST'])
def create_pais():
    data = request.json
    if not data or 'nombre_pais' not in data:
        return jsonify({'error': 'Bad request, falta nombre_pais'}), 400

    nuevo_pais = pais_repo.create_pais(data['nombre_pais'])
    return jsonify({'id': nuevo_pais.id, 'nombre_pais': nuevo_pais.nombre_pais}), 201

@futbol_bp.route('/futbol/<int:pais_id>', methods=['PUT'])
def update_pais(pais_id):
    data = request.json
    if not data or 'nombre_pais' not in data:
        return jsonify({'error': 'Bad request'}), 400

    pais = pais_repo.update_pais(pais_id, data['nombre_pais'])
    if not pais:
        return jsonify({'error': 'País no encontrado'}), 404

    return jsonify({'id': pais.id, 'nombre_pais': pais.nombre_pais}), 200

@futbol_bp.route('/futbol/<int:pais_id>', methods=['DELETE'])
def delete_pais(pais_id):
    pais = pais_repo.delete_pais(pais_id)
    if not pais:
        return jsonify({'error': 'País no encontrado'}), 404

    return jsonify({'result': 'País eliminado'}), 200
