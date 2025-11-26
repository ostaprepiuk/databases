import os

class Config:
    # Отримання конфігурації з app.yml або env vars
    # Для простоти, вказуємо конфігурацію напряму
    
    # !!! ЗАМІНІТЬ ЦІ ЗНАЧЕННЯ НА ВАШІ !!!
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'olia1311')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '127.0.0.1')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'lab3')

    # Конфігурація SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False