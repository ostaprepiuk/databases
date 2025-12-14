from flask import Blueprint, request, jsonify
from app.service.notification_service import NotificationService
from app.dao.user_dao import UserDAO # Для виклику функції середнього віку

notification_bp = Blueprint('notification_bp', __name__)
notification_service = NotificationService()
user_dao = UserDAO()

# Ендпоінт для виклику процедури вставки (Завдання 2.a)
@notification_bp.route('/sp/insert', methods=['POST'])
def add_notification_via_sp():
    data = request.get_json()
    user_id = data.get('user_id')
    priority_level = data.get('priority_level')
    message = data.get('message')

    if not user_id or not message or priority_level is None:
        return jsonify({'message': 'Missing user_id, priority_level, or message'}), 400

    try:
        # При спробі вставити user_id, що закінчується на 00 (наприклад, 100), спрацює ТРИГЕР 3.a
        notification_service.create_notification_via_sp(user_id, priority_level, message)
        return jsonify({'message': 'Notification inserted successfully via SP'}), 201
    except Exception as e:
        return jsonify({'message': f'Database Error (Trigger or SP): {e}'}), 400

# Ендпоінт для виклику функції (Завдання 2.d)
@notification_bp.route('/fn/avg-age', methods=['GET'])
def get_average_age():
    try:
        avg_age = user_dao.get_average_age()
        return jsonify({'average_user_age': float(avg_age)}), 200
    except Exception as e:
        return jsonify({'message': f'Error calling function: {e}'}), 500