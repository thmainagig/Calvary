from flask import Flask
from config import Config
from app.models import db
from flask_mail import Mail

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    mail = Mail(app)

    with app.app_context():
        from app.routes import main_bp
        app.register_blueprint(main_bp)

    return app