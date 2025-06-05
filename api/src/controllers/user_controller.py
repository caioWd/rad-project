from flask_restful import Resource, reqparse
from src.services.user_service import UserService

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str, required=True)
post_parser.add_argument('road', type=str, required=True)
post_parser.add_argument('number', type=str, required=True)
post_parser.add_argument('district', type=str, required=True)
post_parser.add_argument('city', type=str, required=True)
post_parser.add_argument('state', type=str, required=True)
post_parser.add_argument('zipcode', type=str, required=True)
post_parser.add_argument('phone', type=str, required=True)

put_parser = reqparse.RequestParser()
put_parser.add_argument('name', type=str, required=False)
put_parser.add_argument('road', type=str, required=False)
put_parser.add_argument('number', type=str, required=False)
put_parser.add_argument('district', type=str, required=False)
put_parser.add_argument('city', type=str, required=False)
put_parser.add_argument('state', type=str, required=False)
put_parser.add_argument('zipcode', type=str, required=False)
put_parser.add_argument('phone', type=str, required=False)

class UserList(Resource):
    def post(self):
        args = post_parser.parse_args()
        return UserService.create(args)
    
    def get(self):
        return UserService.get_all()

class UserById(Resource):
    def get(self, user_id):
        return UserService.get_by_id(user_id)

    def delete(self, user_id):
        return UserService.delete(user_id)

    def put(self, user_id):
        args = put_parser.parse_args()
        return UserService.update(user_id, args)
        