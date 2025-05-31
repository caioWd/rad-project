from database import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    road = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    district = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    registration_date = db.Column(db.String)
    due_date = db.Column(db.String)
    inactive_date = db.Column(db.String)

    def __init__(self, name, road, number, district, city, state, zipcode, phone):
        self.name = name
        self.road = road
        self.number = number
        self.district = district
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.registration_date = None
        self.due_date = None
        self.inactive_date = None

    @classmethod
    def get_all(cls):
        try:
            return [user.json() for user in cls.query.all()]
        except Exception as e:
            print(f"Erro: {e}")
            raise Exception("Erro ao recuperar dados de usuários do banco.")

    @classmethod
    def get_by_id(cls, user_id):
        try:
            return cls.query.filter_by(id=user_id).first()
        except Exception as e:
            print(f"Erro: {e}")
            raise Exception("Erro ao recuperar dados do usuário do banco.")

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(f"Erro: {e}")
            raise Exception("Erro ao salvar dados do usuário no banco.")

    def update_to_db(self, data):
        try:
            for key, value in data.items():
                if value is not None:
                    setattr(self, key, value)
            db.session.commit()
        except Exception as e:
            print(f"Erro: {e}")
            raise Exception("Erro ao atualizar dados do usuário no banco.")

    def delete_to_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(f"Erro: {e}")
            raise Exception("Erro ao deletar usuário do banco.")

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "road": self.road,
            "number": self.number,
            "district": self.district,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "phone": self.phone
        }