from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

db = SQLAlchemy()
login_manago = LoginManager()
tapatiio = SocketIO(max_http_buffer_size=100 * 1024 * 1024)

def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manago.init_app(app)
    tapatiio.init_app(app)
    from app.routes import main
    app.register_blueprint(main)
    from app.models import User
    @login_manago.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    return app