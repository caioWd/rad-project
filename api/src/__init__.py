from flask import Flask
from src.controllers.test_controller import init_controllers
from src.utils.database import db
from config import Config
    
def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    init_controllers(app)

    with app.app_context():
        db.create_all()

    return app