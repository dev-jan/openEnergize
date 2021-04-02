from flask_restx import Namespace, Api, Resource, fields
from backend.Configuration import get_configuration

api = Namespace('consumers', description='Energy consumers')

consumer = api.model('Consumer', {
    'id': fields.Integer(required=True, description='ID of the producer'),
    'name': fields.String(required=True, description='Name of the producer')
})

CONFIG = get_configuration()

@api.route('/')
class ProducerList(Resource):
    @api.doc('list_consumers')
    @api.marshal_list_with(consumer)
    def get(self):
        return CONFIG['consumers']

@api.route('/<id>')
@api.param('id', 'Identifier of the consumer')
@api.response(404, 'Consumer not found')
class Producer(Resource):
    @api.doc('get_producter')
    @api.marshal_with(consumer)
    def get(self, id):
        for consumer in CONFIG['consumers']:
            if consumer['id'] == int(id):
                return consumer
        api.abort(404)
