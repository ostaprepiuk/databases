from app.dao.owner_dao import OwnerDAO
from app.domain.owner import Owner

class OwnerService:
    def __init__(self):
        self.dao = OwnerDAO()

    def get_all_owners(self):
        return self.dao.find_all()

    def get_owner_by_id(self, owner_id):
        return self.dao.find_by_id(owner_id)

    def create_owner(self, data):
        new_owner = Owner(**data)
        return self.dao.create(new_owner)

    def update_owner(self, owner_id, data):
        owner = self.dao.find_by_id(owner_id)
        if not owner:
            return None
        
        for key, value in data.items():
            setattr(owner, key, value)
            
        return self.dao.update(owner)

    def delete_owner(self, owner_id):
        return self.dao.delete(owner_id)