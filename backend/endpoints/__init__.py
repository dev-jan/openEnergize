from flask_restx import Api, Resource, fields
from .producers import api as producer_api

api = Api(
    title="HSLU Energymanagement API",
    version='1.0',
    description='REST API for the Energymanagement frontend and other interested parties',
    # All API metadatas
)

api.add_namespace(producer_api)
