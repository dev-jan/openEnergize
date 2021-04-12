from flask_restx import Namespace, Api, Resource, fields
from ..producer_adapters.AbstractProducerAdapter import AbstractProducerAdapter
from ..producer_adapters.ConstantValueProducerAdapter import ConstantValueProducerAdapter
from ..Configuration import get_configuration

api = Namespace('storages', description='Energy storages')

storage = api.model('Storage', {
    'id': fields.Integer(required=True, description='ID of the storage'),
    'name': fields.String(required=True, description='Name of the storage'),
    'type': fields.String(required=True,
        description='Type of the storage',
        attribute=lambda x: x['adapter'].get_type()),
    'currentStorageCapacityInPercent': fields.Float(required=False,
        description='Current Storage capacity in percent',
        attribute=lambda x: x['adapter'].get_current_storage_capacity())
})

CONFIG = get_configuration()

@api.route('/')
class StorageList(Resource):
    @api.doc('list_storages')
    @api.marshal_list_with(storage)
    def get(self):
        return CONFIG['storages']
