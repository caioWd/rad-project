# src/services/payment_service.py

from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.models.enrollment import Enrollment
from src.models.payments import Payments
from src.utils.payment_types import PaymentType

class PaymentService:
    @staticmethod
    def make_a_payment(enroll_id, value, type_):

        enrollment = Enrollment.query.get(enroll_id)
        if not enrollment:
            return {'message': 'Matrícula não encontrada.'}, 404
        
        if type_ not in [e.value for e in PaymentType]:
            return {'message': f'Tipo de pagamento inválido. Tipos válidos: {[e.value for e in PaymentType]}'}, 400


        try:
            due_date = datetime.strptime(enrollment.due_date, '%d/%m/%Y')
            new_due_date = due_date + relativedelta(months=1)
            enrollment.due_date = new_due_date.strftime('%d/%m/%Y')

            today = datetime.today()
            if new_due_date < today:
                enrollment.inactive_date = new_due_date.strftime('%d/%m/%Y')
            else:
                enrollment.inactive_date = None

            payment = Payments(
                enrollment_id=enroll_id,
                value=value,
                type=type_
            )

            payment.save_to_db()
            enrollment.save_to_db()

            return {
                'message': 'Pagamento realizado com sucesso.',
                'user': {
                    'id': enrollment.user.id,
                    'name': enrollment.user.name
                },
                'enrollment': {
                    'id': enrollment.id,
                    'due_date': enrollment.due_date,
                    'inactive_date': enrollment.inactive_date
                },
                'payment': payment.json()
            }, 201

        except Exception as e:
            print("Erro ao processar pagamento:", e)
            return {'message': 'Erro ao processar o pagamento.'}, 500
        
    @staticmethod
    def list_payments(enroll_id):
        enrollment = Enrollment.query.get(enroll_id)
        if not enrollment:
            return {'message': 'Matrícula não encontrada.'}, 404

        try:
            payments = Payments.get_all_by_enrollment_id(enroll_id)
            return {
                'enrollment_id': enroll_id,
                'user': {
                    'id': enrollment.user.id,
                    'name': enrollment.user.name
                },
                'payments': payments
            }, 200
        except Exception as e:
            print("Erro ao listar pagamentos:", e)
            return {'message': 'Erro ao buscar pagamentos no banco.'}, 500
