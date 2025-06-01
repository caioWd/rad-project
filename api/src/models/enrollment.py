from database import db

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    registration_date = db.Column(db.String, nullable=False)
    due_date = db.Column(db.String, nullable=False)
    inactive_date = db.Column(db.String)

    user = db.relationship('User', backref=db.backref('enrollments', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, user_id, registration_date, due_date, inactive_date = None):
        self.user_id = user_id
        self.registration_date = registration_date
        self.due_date = due_date
        self.inactive_date = inactive_date
        
    @classmethod    
    def get_all(cls):
        try:
            result = []
            for enrollment in cls.query.all():
                enrollment_data = {
                    'id': enrollment.id,
                    'user_id': enrollment.user_id,
                    'name': enrollment.user.name if enrollment.user else None,
                    'registration_date': enrollment.registration_date,
                    'due_date': enrollment.due_date,
                    'inactive_date': enrollment.inactive_date
                }
                result.append(enrollment_data)
            return result
        except Exception as e:
            print(f"Erro: {e}")
            raise Exception("Erro ao recuperar usuários matriculados no banco.")

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Erro ao salvar matrícula no banco:", str(e))
            raise Exception("Erro ao salvar matrícula de usuário no banco.")
        
    def update_to_db(self, registration_date, due_date, inactive_date):
        try:
            self.registration_date = registration_date
            self.due_date = due_date
            self.inactive_date = inactive_date
            db.session.commit()
        except Exception as e:
            print("Erro ao atualizar matrícula no banco:", str(e))
            raise Exception("Erro ao atualizar matrícula no banco.")
    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'registration_date': self.registration_date,
            'due_date': self.due_date,
            'inactive_date': self.inactive_date
        }
