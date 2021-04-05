from flask_restx import Namespace, Api, Resource, fields
from ..producer_adapters.AbstractProducerAdapter import AbstractProducerAdapter
from ..producer_adapters.ConstantValueProducerAdapter import ConstantValueProducerAdapter
from ..Configuration import get_configuration

api = Namespace('totals', description='Summary of production and consumption')

totals = api.model('Totals', {
    'totalEnergyProduction': fields.Float(required=True, description='Total sum of produced energy at the moment'),
    'totalEnergyConsumption': fields.Float(required=True, description='Total sum of consumed energy at the moment'),
    'energySum': fields.Float(required=True, description='Produced minus consumed energy the moment')
})

CONFIG = get_configuration()

@api.route('/')
class ProducerList(Resource):
    @api.doc('energy_totals')
    @api.marshal_with(totals)
    def get(self):
        consumers = CONFIG['consumers']
        producers = CONFIG['producers']

        totalConsumption = sum(float(c['adapter'].get_current_energy_consumption()) for c in consumers)
        totalProduction = sum(float(p['adapter'].get_current_energy_production()) for p in producers)

        return {
            'totalEnergyProduction': totalProduction,
            'totalEnergyConsumption': totalConsumption,
            'energySum': totalProduction - totalConsumption
        }
