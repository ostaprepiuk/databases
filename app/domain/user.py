from app import db
from app.domain.smartwatch import SmartwatchUser 

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(100), nullable=False, index=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.Enum('male', 'female', 'other'), nullable=True)
    relation_to_owner = db.Column(db.String(50), nullable=True)

    used_smartwatches = db.relationship(
        'Smartwatch',
        secondary=SmartwatchUser.__tablename__,
        back_populates='users'
    )

    def __repr__(self):
        return f"<User {self.user_id}: {self.full_name}>"