from app import db 
from app.domain.owner import Owner

class OwnerDAO:
    # 1. CREATE
    def create(self, owner: Owner):
        db.session.add(owner)
        db.session.commit()
        return owner

    # 2. READ ALL
    def find_all(self):
        return Owner.query.all()

    # 3. READ BY ID
    def find_by_id(self, owner_id):
        return Owner.query.get(owner_id)

    # 4. UPDATE
    def update(self, owner: Owner):
        db.session.commit()
        return owner

    # 5. DELETE
    def delete(self, owner_id):
        owner = self.find_by_id(owner_id)
        if owner:
            db.session.delete(owner)
            db.session.commit()
            return True
        return False