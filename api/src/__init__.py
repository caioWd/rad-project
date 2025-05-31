from flask import Flask
from src.controllers.person import PersonList, Person
from database import db
from config import Config
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(PersonList, '/persons')
api.add_resource(Person, '/persons/<person_id>')