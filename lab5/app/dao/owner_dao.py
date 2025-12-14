from app import db 
from app.domain.owner import Owner

class OwnerDAO:
    def create(self, owner: Owner):
        db.session.add(owner)
        db.session.commit()
        return owner

    def find_all(self):
        return Owner.query.all()

    def find_by_id(self, owner_id):
        return Owner.query.get(owner_id)

    def update(self, owner: Owner):
        db.session.commit()
        return owner

    def delete(self, owner_id):
        owner = self.find_by_id(owner_id)
        if owner:
            db.session.delete(owner)
            db.session.commit()
            return True
        return False