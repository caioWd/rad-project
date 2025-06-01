from src.models.user import User

class UserService:
    @staticmethod
    def create(data):
        if User.query.filter_by(name=data['name']).first():
            return {'message': 'Nome já cadastrado.'}, 400

        if User.query.filter_by(phone=data['phone']).first():
            return {'message': 'Telefone já cadastrado.'}, 400

        try:
            user = User(data['name'], 
                        data['road'], 
                        data['number'], 
                        data['district'], 
                        data['city'], 
                        data['state'],
                        data['zipcode'],
                        data['phone']
                    )
            
            user.save_to_db()
            return {'message': 'Usuário criado com sucesso.', 'user': user.json()}, 201
        except Exception as e:
            return {'message': str(e)}, 500

    @staticmethod
    def get_all():
        try:
            users = User.get_all()
            return users, 200
        except Exception as e:
            return {'message': str(e)}, 500

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.get_by_id(user_id)
            if not user:
                return {'message': 'Usuário não encontrado.'}, 404
            return user.json(), 200
        except Exception as e:
            return {'message': str(e)}, 500

    @staticmethod
    def update(user_id, data):
        user = User.get_by_id(user_id)
        if not user:
            return {'message': 'Usuário não encontrado.'}, 404

        if 'name' in data:
            existing = User.query.filter_by(name=data['name']).first()
            if existing and existing.id != user_id:
                return {'message': 'Nome já cadastrado.'}, 400

        if 'phone' in data:
            existing = User.query.filter_by(phone=data['phone']).first()
            if existing and existing.id != user_id:
                return {'message': 'Telefone já cadastrado.'}, 400
        try:
            user.update_to_db(data)
            return user.json(), 200
        except Exception as e:
            print("Erro ao atualizar no banco:", e)
            return {'message': 'Erro ao atualizar dados no banco.'}, 500

    @staticmethod
    def delete(user_id):
        try:
            user = User.get_by_id(user_id)
            if not user:
                return {'message': 'Usuário não encontrado.'}, 404
            
            enrollment = user.enrollments[0] if user.enrollments else None
            if enrollment and not enrollment.inactive_date:
                return {'message': 'Usuário não pode ser deletado. Matrícula ainda está ativa.'}, 400
            
            user.delete_to_db()
            return {'message': 'Usuário deletado com sucesso.'}, 200
        except Exception as e:
            print("Erro ao deletar usuário:", e) 
            return {'message': str(e)}, 500