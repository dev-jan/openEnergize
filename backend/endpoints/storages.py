from flask_restx import Namespace, Resource, fields
from ..Configuration import get_configuration

api = Namespace('storages', description='Energy storages')

storage = api.model('Storage', {
    'id': fields.Integer(required=True, description='ID of the storage'),
    'name': fields.String(required=True, description='Name of the storage'),
    'type': fields.String(
        required=True,
        description='Type of the storage',
        attribute=lambda x: x['adapter'].get_type()
    ),
    'currentStorageCapacityInPercent': fields.Float(
        required=False,
        description='Current Storage capacity in percent',
        attribute=lambda x: x['adapter'].get_current_storage_capacity()
    )
})


@api.route('/')
class StorageList(Resource):
    @api.doc('list_storages')
    @api.marshal_list_with(storage)
    def get(self):
        return get_configuration()['storages']
