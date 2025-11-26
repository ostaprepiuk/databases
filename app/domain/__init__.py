# app/domain/__init__.py

# Примусово імпортуємо всі моделі, щоб SQLAlchemy їх побачила
# (Це вирішує проблему ранньої реєстрації)
from .owner import Owner
from .address import Address
from .user import User
from .smartwatch import Smartwatch, SmartwatchUser

# Зверніть увагу: тут не потрібно додавати db.Model, лише імпорти