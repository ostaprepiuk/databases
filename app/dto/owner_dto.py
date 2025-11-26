from app import ma 
from app.domain.owner import Owner

# Схема для серіалізації/десеріалізації об'єкта Owner
class OwnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Owner
        load_instance = True
        include_fk = True

class OwnerDetailsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Owner
        load_instance = True
        include_relationships = True
        include_fk = True

owner_schema = OwnerSchema()
owners_schema = OwnerSchema(many=True)
owner_details_schema = OwnerDetailsSchema()