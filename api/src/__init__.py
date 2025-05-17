from flask import Flask
from src.controllers.test_controller import init_controllers
    
def createApp():
    app = Flask(__name__)

    init_controllers(app)

    return app