from database import db

class PersonModel(db.Model):
    __tablename__ = 'person'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    
    def __init__(self, name, address, city, state, phone):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.phone = phone
    
    @classmethod
    def get_all(cls):
        return [person.json() for person in cls.query.all()]
    
    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            print("Erro ao filtrar pessoa por ID", e)
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "phone": self.phone
        }
            
    def update_to_db(self, data):
        try:
            for key, value in data.items():
                setattr(self, key, value)
            db.session.commit()
        except Exception as e:
            print("Erro ao atualizar pessoa", e)
    
    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Erro ao cadastrar pessoa", e)
    
    def delete_to_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print("Erro ao deletar pessoa", e)
            