# controllers/users_controllers.py
import logging
from services.users_services import UsersService
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

service = UsersService()

user_bp = Blueprint('users', __name__)

# ------------------- LOGIN -------------------
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400

    user = service.authenticate_user(username, password)
    if user:
        # ✅ identity ahora es un string (para evitar el error "Subject must be a string")
        access_token = create_access_token(identity=str(user.id))
        return jsonify({'access_token': access_token}), 200

    return jsonify({'error': 'Credenciales inválidas'}), 401


# ------------------- OBTENER TODOS LOS USUARIOS -------------------
@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()  # ✅ obtiene el id del token
    logger.info(f"Usuario autenticado con ID: {current_user_id}")

    users = service.get_all_users()
    return jsonify([{'id': u.id, 'username': u.username} for u in users]), 200


# ------------------- OBTENER USUARIO POR ID -------------------
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404


# ------------------- REGISTRAR USUARIO -------------------
@user_bp.route('/registry', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400

    user = service.create_user(username, password)
    return jsonify({'id': user.id, 'username': user.username}), 201


# ------------------- ACTUALIZAR USUARIO -------------------
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = service.update_user(user_id, username, password)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404


# ------------------- ELIMINAR USUARIO -------------------
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = service.delete_user(user_id)
    if user:
        return jsonify({'message': 'Usuario eliminado correctamente'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404
