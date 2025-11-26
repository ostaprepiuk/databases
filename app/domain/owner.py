from app import db 
from datetime import datetime

class Owner(db.Model):
    __tablename__ = 'owners'
    
    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False, index=True)
    date_of_birth = db.Column(db.Date, nullable=True)

    smartwatches = db.relationship('Smartwatch', backref='owner', lazy=True)

    def __repr__(self):
        return f"<Owner {self.owner_id}: {self.full_name}>"