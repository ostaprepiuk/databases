from app.domain.user import User
from app.domain.smartwatch import Smartwatch
from app.domain.address import Address
from app import db 
from sqlalchemy import func

class UserDAO:
    # Базовий READ
    def find_all(self):
        return User.query.all()
    
    # 1. Запит M:1 (Місто -> Користувачі)
    def get_users_by_city(self):
        results = db.session.query(
            Address.city,
            func.group_concat(User.full_name.distinct().label('current_users'))
        ).join(Smartwatch, Address.address_id == Smartwatch.address_id)\
         .join(Smartwatch.users)\
         .group_by(Address.city)\
         .all()
         
        return [{'city': city, 'users': users.split(', ')} for city, users in results]
    
    # 2. Запит M:M (Годинник -> Користувачі)
    def get_watch_users(self):
        results = db.session.query(
            Smartwatch.serial_number,
            Smartwatch.model,
            func.group_concat(User.full_name.distinct().label('all_users'))
        ).join(Smartwatch.users)\
         .group_by(Smartwatch.watch_id)\
         .all()
         
        return [{'serial_number': sn, 'model': model, 'users': users.split(', ')} for sn, model, users in results]