# app/service/notification_service.py

from app.dao.notification_dao import NotificationDAO

class NotificationService:
    def __init__(self):
        self.dao = NotificationDAO()

    # Метод для виклику збереженої процедури вставки (Завдання 2.a)
    def create_notification_via_sp(self, user_id: int, priority_level: int, message: str):
        # Тут може бути додаткова бізнес-логіка, але зараз просто викликаємо DAO
        return self.dao.insert_with_sp(user_id, priority_level, message)

    # Ви можете додати інші методи, якщо NotificationController їх вимагає
    # ...