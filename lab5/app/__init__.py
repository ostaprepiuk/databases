# app/__init__.py (Виправлена версія)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import config
Config = config.Config 

# Ініціалізація розширень (глобально)
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    # 1. Створюємо екземпляр Flask під новою назвою
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    # 2. Прив'язка розширень
    db.init_app(flask_app)
    ma.init_app(flask_app)

    # 3. Імпорт моделей
    import app.domain 

    # 4. Реєстрація контролерів (Blueprint)
    from app.controller.owner_controller import owner_bp
    from app.controller.user_controller import user_bp

    # 5. Реєстрація Blueprint на новій змінній
    flask_app.register_blueprint(owner_bp, url_prefix='/api/v1/owners')
    flask_app.register_blueprint(user_bp, url_prefix='/api/v1/users')

    return flask_app