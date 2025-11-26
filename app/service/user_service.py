from app.dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.dao = UserDAO()

    # M:1
    def get_users_by_city_report(self):
        return self.dao.get_users_by_city()

    # M:M
    def get_watch_users_report(self):
        return self.dao.get_watch_users()