from app import db 
from datetime import datetime

# Стикувальна таблиця M:M
class SmartwatchUser(db.Model):
    __tablename__ = 'smartwatches_users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    watch_id = db.Column(db.Integer, db.ForeignKey('smartwatches.watch_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

    __table_args__ = (
        db.UniqueConstraint('watch_id', 'user_id', 'start_date', name='idx_swu_unique'),
    )


class Smartwatch(db.Model):
    __tablename__ = 'smartwatches'
    
    watch_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.owner_id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.address_id'), nullable=True)
    registered_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    users = db.relationship(
        'User',
        secondary='smartwatches_users',
        back_populates='used_smartwatches'
    )

    def __repr__(self):
        return f"<Smartwatch {self.watch_id}: {self.serial_number}, Model: {self.model}>"