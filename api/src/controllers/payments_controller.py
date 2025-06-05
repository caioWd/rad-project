from flask_restful import Resource, reqparse
from src.services.payments_service import PaymentService

class Payment(Resource):
    def post(self, enroll_id):
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=str, required=True, help='O campo "value" é obrigatório.')
        parser.add_argument('type', type=str, required=True, help='O campo "type" é obrigatório.')
        data = parser.parse_args()

        return PaymentService.make_a_payment(
            enroll_id=enroll_id,
            value=data['value'],
            type_=data['type']
        )
    
    def get(self, enroll_id):
        return PaymentService.list_payments(enroll_id)