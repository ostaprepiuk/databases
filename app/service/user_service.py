from app.dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def get_users_by_city_report(self):
        return self.dao.get_users_by_city()

    def get_watch_users_report(self):
        return self.dao.get_watch_users()