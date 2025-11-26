from flask import Blueprint, jsonify
from app.service.user_service import UserService

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()

# M:1 Звіт (Місто -> Користувачі)
@user_bp.route('/report/by-city', methods=['GET'])
def get_users_by_city_report():
    report = user_service.get_users_by_city_report()
    return jsonify(report)

# M:M Звіт (Годинник -> Користувачі)
@user_bp.route('/report/watch-usage', methods=['GET'])
def get_watch_users_report():
    report = user_service.get_watch_users_report()
    return jsonify(report)