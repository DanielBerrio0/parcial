from flask import Blueprint

futbol_bp= Blueprint('futbol_bp',__name__)

@futbol_bp.route('/futbol', methods=['GET'])

@futbol_bp.route('/futbol/<int:pais_id>', methods=['GET'])

@futbol_bp.route('/futbol', methods=['POST'])

@futbol_bp.route('/futbol/<int:pais_id>', methods=['PUT'])

@futbol_bp.route('/futbol/<int:pais_id>', methods=['DELETE'])
