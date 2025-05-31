from flask import Flask
from src.controllers.user_controller import UserById, UserList
from database import db
from config import Config
from flask_restful import Api

app = Flask(__name__)
api = Api(app, prefix="/crossx/api")
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(UserList, '/users')
api.add_resource(UserById, '/users/<int:user_id>')