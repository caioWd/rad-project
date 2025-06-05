from database import db
from datetime import datetime, timezone

class Payments(db.Model):
    __tablename__ = 'payments'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollments.id'), nullable=False)
    value = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    payment_date = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    enrollment = db.relationship('Enrollment', backref=db.backref('payments', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, enrollment_id, value, type):
        self.enrollment_id = enrollment_id
        self.value = value
        self.type = type

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Erro ao salvar pagamento:", str(e))
            raise Exception("Erro ao salvar pagamento no banco.")
        
    @classmethod
    def get_all_by_enrollment_id(cls, enrollment_id):
        try:
            payments = cls.query.filter_by(enrollment_id=enrollment_id).all()
            return [payment.json() for payment in payments]
        except Exception as e:
            print(f"Erro ao buscar pagamentos: {e}")
            raise Exception("Erro ao buscar pagamentos no banco.")

    def json(self):
        return {
            'id': self.id,
            'enrollment_id': self.enrollment_id,
            'value': self.value,
            'type': self.type,
            'payment_date': self.payment_date.strftime('%d-%m-%y')
        }
