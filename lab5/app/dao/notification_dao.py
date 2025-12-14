from app import db 
from sqlalchemy import text

class NotificationDAO:
    # Виклик збереженої процедури для вставки (Завдання 2.a)
    def insert_with_sp(self, user_id: int, priority_level: int, message: str):
        try:
            # Викликаємо процедуру sp_insert_notification
            db.session.execute(
                text('CALL sp_insert_notification(:uid, :priority, :msg)'),
                {'uid': user_id, 'priority': priority_level, 'msg': message}
            )
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e