from flask_restx import Api
from .producers import ns as producer_namespace

api = Api(
    title="HSLU Energymanagement API",
    version='1.0',
    description='REST API for the Energymanagement frontend and other interested parties',
    # All API metadatas
)

api.add_namespace(producer_namespace)
