from flask_restful import Resource, reqparse
from src.services.enrollment_service import EnrollmentService

post_parser = reqparse.RequestParser()
post_parser.add_argument('user_id', type=int, required=True)
post_parser.add_argument('registration_date', type=str, required=True)

class Enrollment(Resource):
    def post(self):
        args = post_parser.parse_args()
        return EnrollmentService.enrollUser(args)
     
    def get(self):
        return EnrollmentService.getEnrollments()
    
    def put(self):
        args = post_parser.parse_args()
        return EnrollmentService.updateUserEnrollent(args)
        