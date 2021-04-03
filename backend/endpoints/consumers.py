from flask_restx import Namespace, Api, Resource, fields
from ..Configuration import get_configuration

api = Namespace('consumers', description='Energy consumers')

consumer = api.model('Consumer', {
    'id': fields.Integer(required=True, description='ID of the producer'),
    'name': fields.String(required=True, description='Name of the producer'),
    'type': fields.String(required=True,
        description='Type of the consumer',
        attribute=lambda x: x['adapter'].get_type()),
    'currentConsumptionInWatt': fields.Float(required=False,
        description='Current power measurement in Watt',
        attribute=lambda x: x['adapter'].get_current_energy_consumption())
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
