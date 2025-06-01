from src.models.user import User
from src.models.enrollment import Enrollment
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EnrollmentService:
    @staticmethod
    def enrollUser(data):
        user_id = data.get('user_id')
        if not user_id:
            return {'message': 'O campo "user_id" é obrigatório.'}, 400

        user = User.get_by_id(user_id)
        if not user:
            return {'message': 'Usuário não encontrado.'}, 404

        existing_enrollment = Enrollment.query.filter_by(user_id=user_id).first()
        if existing_enrollment:
            print(f"Usuário {user_id} já matriculado, interrompendo fluxo.")
            return {'message': 'Usuário já está matriculado.'}, 400

        registration_date_str = data.get('registration_date')
        if not registration_date_str:
            return {'message': 'O campo "registration_date" é obrigatório.'}, 400

        try:
            registration_date = datetime.strptime(registration_date_str, '%d/%m/%Y')
        except ValueError:
            return {'message': 'Formato inválido para "registration_date". Use "dd/mm/yyyy".'}, 400

        due_date = registration_date + relativedelta(months=1)
        today = datetime.today()
    
        inactive_date_str = due_date.strftime('%d/%m/%Y') if due_date < today else None

        enrollment = Enrollment(
            user_id=user_id,
            registration_date=registration_date_str,
            due_date=due_date.strftime('%d/%m/%Y'),
            inactive_date=inactive_date_str
        )

        try:
            enrollment.save_to_db()
            return {
                'message': 'Usuário matriculado com sucesso.',
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'enrollment': {
                        'id': enrollment.id,
                        'registration_date': enrollment.registration_date,
                        'due_date': enrollment.due_date,
                        'inactive_date': enrollment.inactive_date
                    }
                }
            }, 201

        except Exception as e:
            print("Erro ao salvar matrícula no banco:", e)
            return {'message': 'Erro ao salvar dados de matrícula no banco.'}, 500

    def getEnrollments():
        try:
            enrollments = Enrollment.get_all()
            return enrollments, 200
        except Exception as e:
            return {'message': str(e)}, 500
        

    def updateUserEnrollent(data):

        user_id = data.get('user_id')
        if not user_id:
            return {'message': 'O campo "user_id" é obrigatório.'}, 400

        user = User.get_by_id(user_id)
        if not user:
            return {'message': 'Usuário não encontrado.'}, 404

        registration_date_str = data.get('registration_date')
        if not registration_date_str:
            return {'message': 'O campo "registration_date" é obrigatório.'}, 400

        try:
            registration_date = datetime.strptime(registration_date_str, '%d/%m/%Y')
        except ValueError:
            return {'message': 'Formato inválido para "registration_date". Use "dd/mm/yyyy".'}, 400

        enrollment = Enrollment.query.filter_by(user_id=user_id).first()
        if not enrollment:
            return {'message': 'Usuário não possui matrícula.'}, 404

        due_date = registration_date + relativedelta(months=1)
        today = datetime.today()

        inactive_date_str = due_date.strftime('%d/%m/%Y') if due_date < today else None
        try:
            enrollment.update_to_db(
                registration_date=registration_date_str,
                due_date=due_date.strftime('%d/%m/%Y'),
                inactive_date=inactive_date_str
            )
            return {
                'message': 'Matrícula atualizada com sucesso.',
                'enrollment': enrollment.json()
            }, 200
        except Exception as e:
            return {'message': 'Erro ao atualizar matrícula.'}, 500

            