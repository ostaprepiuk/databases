from flask import Blueprint, request, jsonify
from app.service.owner_service import OwnerService
from app.dto.owner_dto import owner_schema, owners_schema

owner_bp = Blueprint('owner_bp', __name__)
owner_service = OwnerService()

@owner_bp.route('/', methods=['GET'])
def get_owners():
    owners = owner_service.get_all_owners()
    return jsonify(owners_schema.dump(owners))

@owner_bp.route('/<int:owner_id>', methods=['GET'])
def get_owner(owner_id):
    owner = owner_service.get_owner_by_id(owner_id)
    if owner:
        return jsonify(owner_schema.dump(owner))
    return jsonify({'message': 'Owner not found'}), 404

@owner_bp.route('/', methods=['POST'])
def add_owner():
    data = request.get_json()
    try:
        new_owner = owner_service.create_owner(data)
        return jsonify(owner_schema.dump(new_owner)), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@owner_bp.route('/<int:owner_id>', methods=['PUT'])
def update_owner(owner_id):
    data = request.get_json()
    updated_owner = owner_service.update_owner(owner_id, data)
    if updated_owner:
        return jsonify(owner_schema.dump(updated_owner))
    return jsonify({'message': 'Owner not found'}), 404


@owner_bp.route('/<int:owner_id>', methods=['DELETE'])
def delete_owner(owner_id):
    if owner_service.delete_owner(owner_id):
        return jsonify({'message': 'Дані власника успішно видалено'}), 200
    
    return jsonify({'message': 'Owner not found'}), 404