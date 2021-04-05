from flask_restx import Api, Resource, fields
from .producers import api as producer_api
from .consumers import api as consumer_api
from .totals import api as totals_api

api = Api(
    title="HSLU Energymanagement API",
    version='1.0',
    description='REST API for the Energymanagement frontend and other interested parties',
    # All API metadatas
)

api.add_namespace(producer_api)
api.add_namespace(consumer_api)
api.add_namespace(totals_api)
