from flask_restx import Namespace, Resource, fields
from ..Configuration import get_raw_configuration

api = Namespace('configuration', description='Application configuration')

configuration = api.model('Configuration', {
    'raw': fields.String(required=True, description='Raw Configration content')
})


@api.route('/')
class Configuration(Resource):
    @api.doc('configuration')
    @api.marshal_with(configuration)
    def get(self):
        return {'raw': get_raw_configuration()}
