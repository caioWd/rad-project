from flask import Flask
from config import Config
from database import db
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "Hello world"