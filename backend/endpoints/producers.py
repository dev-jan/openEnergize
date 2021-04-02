from flask_restx import Namespace, Api, Resource, fields
from backend.producer_adapters.AbstractProducerAdapter import AbstractProducerAdapter
from backend.producer_adapters.ConstantValueProducerAdapter import ConstantValueProducerAdapter

api = Namespace('producers', description='Energy producers')

producer = api.model('Producer', {
    'id': fields.Integer(required=True, description='ID of the producer'),
    'name': fields.String(required=True, description='Name of the producer'),
    'type': fields.String(required=True,
        description='Type of the producter',
        attribute=lambda x: x.adapter.get_type()),
    'currentProductionInWatt': fields.Float(required=False,
        description='Current power measurement in Watt',
        attribute=lambda x: x.adapter.get_current_energy_production())
})

class ProducerObject(object):
    def __init__(self, id: int, name: str, adapter: AbstractProducerAdapter):
        self.id = id
        self.name = name
        self.adapter = adapter


# TODO: Move to configuration
PRODUCERS = [
    ProducerObject(0, "Testproducer", ConstantValueProducerAdapter({'value': '236.5'})),
    ProducerObject(1, "Second producer", ConstantValueProducerAdapter({'value': '0.35'}))
]

@api.route('/')
class ProducerList(Resource):
    @api.doc('list_producers')
    @api.marshal_list_with(producer)
    def get(self):
        return PRODUCERS

@api.route('/<id>')
@api.param('id', 'Identifier of the producer')
@api.response(404, 'Producer not found')
class Producer(Resource):
    @api.doc('get_producter')
    @api.marshal_with(producer)
    def get(self, id):
        for producer in PRODUCERS:
            if producer.id == int(id):
                return producer
        api.abort(404)
