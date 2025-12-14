from flask import Blueprint, jsonify
from app.service.user_service import UserService # Потрібно оновити, щоб імпортувати
from app.dao.user_dao import UserDAO # Прямий імпорт для нових функцій

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()
user_dao = UserDAO()

# M:1 Звіт
@user_bp.route('/report/by-city', methods=['GET'])
def get_users_by_city_report():
    report = user_service.get_users_by_city_report()
    return jsonify(report)

# M:M Звіт
@user_bp.route('/report/watch-usage', methods=['GET'])
def get_watch_users_report():
    report = user_service.get_watch_users_report()
    return jsonify(report)

# НОВИЙ ЗВІТ: Name+No (Завдання 2.c)
@user_bp.route('/report/name-no', methods=['GET'])
def get_name_no_report():
    report = user_dao.get_name_no_report()
    return jsonify(report)