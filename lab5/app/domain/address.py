from app import db

class Address(db.Model):
    __tablename__ = 'addresses'
    
    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    house_number = db.Column(db.String(10), nullable=False)
    apartment = db.Column(db.String(10), nullable=True)
    postal_code = db.Column(db.String(10), nullable=False)
    
    smartwatches = db.relationship('Smartwatch', backref='address', lazy=True)

    def __repr__(self):
        return f"<Address {self.address_id}: {self.city}, {self.street}>"