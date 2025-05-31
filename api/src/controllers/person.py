from flask_restful import Resource, reqparse
from src.models.person import PersonModel

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('address', type=str, required=True)
parser.add_argument('city', type=str, required=True)
parser.add_argument('state', type=str, required=True)
parser.add_argument('phone', type=str, required=True)

class Person(Resource):
    def get(self, person_id):
        try:
            person = PersonModel.get_by_id(person_id)
            return person.json()
        except Exception as e:
            print('Erro ao recuperar dado', e)
            return {'message': 'Erro ao recuperar dado.'}, 500
    
    def delete(self, person_id):
        try:
            person = PersonModel.get_by_id(person_id)
            person.delete_to_db()
            return {
                'message': 'Pessoa deletada com sucesso!'
            },200
        except Exception as e:
            print('Erro ao deletar dado', e)
            return {'message': 'Erro ao deletar dado.'}, 500
    
    def put(self, person_id):
        try:
            args = parser.parse_args()
            person = PersonModel.get_by_id(person_id)
            
            data = {
                "name": args['name'],
                "address": args['address'],
                "city": args['city'],
                "state": args['state'],
                "phone": args['phone'],
            }
            
            person.update_to_db(data)
            return person.json()
            
        except Exception as e:
            print('Erro ao atualizar dado', e)
            return {'message': 'Erro ao atualizar dado.'}, 500
        
class PersonList(Resource):
    def get(self):
        try:
            return PersonModel.get_all() 
        except Exception as e:
            print('Erro ao recuperar dados', e)
            return {'message': 'Erro ao recuperar dados.'}, 500
    
    def post(self):
        try:
            args = parser.parse_args()
            
            name = args['name']
            address = args['address']
            city = args['city']
            state = args['state']
            phone = args['phone']
            
            person = PersonModel(name, address, city, state, phone)
            person.save_to_db()
            
            return {
                'message': 'Pessoa adicionada com sucesso!',
                "person": person.json()
            }, 201
            
        except Exception as e:
            print('Erro ao inserir dados', e)
            return {'message': 'Erro ao inserir dados.'}, 500
        