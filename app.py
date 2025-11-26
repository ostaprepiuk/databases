# app.py (КОРЕНЕВИЙ)

from app import create_app

if __name__ == '__main__':
    flask_app_instance = create_app()
    flask_app_instance.run(debug=True)