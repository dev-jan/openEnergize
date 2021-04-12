from flask_restx import Namespace, Api, Resource, fields
from ..producer_adapters.AbstractProducerAdapter import AbstractProducerAdapter
from ..producer_adapters.ConstantValueProducerAdapter import ConstantValueProducerAdapter
from ..Configuration import get_configuration

api = Namespace('producers', description='Energy producers')

producer = api.model('Producer', {
    'id': fields.Integer(required=True, description='ID of the producer'),
    'name': fields.String(required=True, description='Name of the producer'),
    'type': fields.String(required=True,
        description='Type of the producter',
        attribute=lambda x: x['adapter'].get_type()),
    'currentProductionInWatt': fields.Float(required=False,
        description='Current power measurement in Watt',
        attribute=lambda x: x['adapter'].get_current_energy_production())
})

@api.route('/')
class ProducerList(Resource):
    @api.doc('list_producers')
    @api.marshal_list_with(producer)
    def get(self):
        return get_configuration()['producers']

@api.route('/<id>')
@api.param('id', 'Identifier of the producer')
@api.response(404, 'Producer not found')
class Producer(Resource):
    @api.doc('get_producter')
    @api.marshal_with(producer)
    def get(self, id):
        for producer in get_configuration()['producers']:
            if producer['id'] == int(id):
                return producer
        api.abort(404)
