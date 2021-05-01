from flask_restx import Namespace, Resource, fields
from ..Configuration import get_configuration

api = Namespace('totals', description='Summary of production and consumption')

totals = api.model('Totals', {
    'totalEnergyProduction': fields.Float(
        required=True,
        description='Total sum of produced energy at the moment'
    ),
    'totalEnergyConsumption': fields.Float(
        required=True,
        description='Total sum of consumed energy at the moment'
    ),
    'energySum': fields.Float(
        required=True,
        description='Produced minus consumed energy the moment'
    )
})


@api.route('/')
class ProducerList(Resource):
    @api.doc('energy_totals')
    @api.marshal_with(totals)
    def get(self):
        config = get_configuration()
        consumers = config['consumers']
        producers = config['producers']

        total_consumption = sum(
            float(c['adapter'].get_current_energy_consumption())
            for c in consumers
        )
        total_production = sum(
            float(p['adapter'].get_current_energy_production())
            for p in producers
        )

        return {
            'totalEnergyProduction': total_production,
            'totalEnergyConsumption': total_consumption,
            'energySum': total_production - total_consumption
        }
