from app.domain.user import User
from app.domain.smartwatch import Smartwatch
from app.domain.address import Address
from app import db 
from sqlalchemy import func, text

class UserDAO:
    def find_all(self):
        return User.query.all()
    
    def get_users_by_city(self):
        results = db.session.query(
            Address.city,
            func.group_concat(User.full_name.distinct().label('current_users'))
        ).join(Smartwatch, Address.address_id == Smartwatch.address_id)\
         .join(Smartwatch.users)\
         .group_by(Address.city)\
         .all()
         
        return [{'city': city, 'users': users.split(', ')} for city, users in results]
    
    def get_watch_users(self):
        results = db.session.query(
            Smartwatch.serial_number,
            Smartwatch.model,
            func.group_concat(User.full_name.distinct().label('all_users'))
        ).join(Smartwatch.users)\
         .group_by(Smartwatch.watch_id)\
         .all()
         
        return [{'serial_number': sn, 'model': model, 'users': users.split(', ')} for sn, model, users in results]
    
    # Виклик користувацької функції (Завдання 2.d)
    def get_average_age(self):
        result = db.session.execute(text('SELECT fn_average_user_age()')).scalar()
        return float(result) if result else 0.0

    # Створення звітних стрічок Name+No (Завдання 2.c)
    def get_name_no_report(self):
        results = db.session.execute(
            text("SELECT CONCAT('Noname', user_id) AS Generated_Name FROM users LIMIT 10")
        ).fetchall()
        return [{'generated_name': r[0]} for r in results]