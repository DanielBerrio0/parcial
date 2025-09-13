from flask import Blueprint, jsonify, request
from repository.futbol_repository import PaisRepository
from extensions import db
from models.futbol_model import Mundiales

futbol_bp = Blueprint("futbol_bp", __name__)
pais_repo = PaisRepository()

# Obtener todos los países con sus mundiales
@futbol_bp.route("/", methods=["GET"])
def get_paises():
    paises = pais_repo.get_all_paises()
    resultado = []
    for p in paises:
        resultado.append({
            "id": p.id,
            "nombre_pais": p.nombre_pais,
            "mundiales": [
                {"id": m.id, "title": m.title, "pais_id": m.pais_id}
                for m in p.mundiales
            ]
        })
    return jsonify(resultado), 200

# Obtener un país por ID con sus mundiales
@futbol_bp.route("/<int:pais_id>", methods=["GET"])
def get_pais(pais_id):
    pais = pais_repo.get_pais_by_id(pais_id)
    if not pais:
        return jsonify({"error": "La selección no se encontró"}), 404
    
    return jsonify({
        "id": pais.id,
        "nombre_pais": pais.nombre_pais,
        "mundiales": [
            {"id": m.id, "title": m.title, "pais_id": m.pais_id}
            for m in pais.mundiales
        ]
    }), 200

# Crear país
@futbol_bp.route("/", methods=["POST"])
def create_pais():
    data = request.json
    if not data or "nombre_pais" not in data:
        return jsonify({"error": "Falta el campo nombre_pais"}), 400
    
    nuevo_pais = pais_repo.create_pais(data["nombre_pais"])
    
    return jsonify({
        "id": nuevo_pais.id,
        "nombre_pais": nuevo_pais.nombre_pais,
        "mundiales": []
    }), 201

# Crear un mundial asociado a un país
@futbol_bp.route("/<int:pais_id>/mundiales", methods=["POST"])
def create_mundial(pais_id):
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Falta el campo title"}), 400

    pais = pais_repo.get_pais_by_id(pais_id)
    if not pais:
        return jsonify({"error": "País no encontrado"}), 404

    nuevo_mundial = Mundiales(title=data["title"], pais_id=pais.id)

    db.session.add(nuevo_mundial)
    db.session.commit()

    return jsonify({
        "id": nuevo_mundial.id,
        "title": nuevo_mundial.title,
        "pais_id": nuevo_mundial.pais_id
    }), 201

# Actualizar país
@futbol_bp.route("/<int:pais_id>", methods=["PUT"])
def update_pais(pais_id):
    data = request.json
    if not data or "nombre_pais" not in data:
        return jsonify({"error": "Falta el campo nombre_pais"}), 400
    
    pais = pais_repo.update_pais(pais_id, data["nombre_pais"])
    if not pais:
        return jsonify({"error": "País no encontrado"}), 404
    
    return jsonify({
        "id": pais.id,
        "nombre_pais": pais.nombre_pais,
        "mundiales": [
            {"id": m.id, "title": m.title, "pais_id": m.pais_id}
            for m in pais.mundiales
        ]
    }), 200

# Eliminar país
@futbol_bp.route("/<int:pais_id>", methods=["DELETE"])
def delete_pais(pais_id):
    pais = pais_repo.delete_pais(pais_id)
    if not pais:
        return jsonify({"error": "País no encontrado"}), 404
    
    return jsonify({"result": "País eliminado"}), 200
