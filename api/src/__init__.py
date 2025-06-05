from flask import Flask
from src.controllers.user_controller import UserById, UserList
from src.controllers.enrollment_controller import Enrollment
from src.controllers.payments_controller import Payment
from database import db
from config import Config
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app, prefix="/crossx/api")
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(UserList, '/users')
api.add_resource(UserById, '/users/<int:user_id>')
api.add_resource(Enrollment, '/enrollments')
api.add_resource(Payment, '/enrollments/<int:enroll_id>/payments')
