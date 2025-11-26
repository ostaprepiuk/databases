from app import ma 
from app.domain.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

class UserWithWatchesSchema(ma.SQLAlchemyAutoSchema):
    used_smartwatches = ma.Nested('SmartwatchSchema', many=True, exclude=('users',))

    class Meta:
        model = User
        load_instance = True
        include_relationships = True
        include_fk = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_watches_schema = UserWithWatchesSchema(many=True)

class SmartwatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        from app.domain.smartwatch import Smartwatch
        model = Smartwatch
        load_instance = True
        fields = ('watch_id', 'serial_number', 'model')