from flask_restx import Api
from .producers import api as producer_api
from .consumers import api as consumer_api
from .storages import api as storage_api
from .totals import api as totals_api
from .events import api as events_api

api = Api(
    title="HSLU Energymanagement API",
    version='1.0',
    description='REST API for the Energymanagement frontend',
    # All API metadatas
)

api.add_namespace(producer_api)
api.add_namespace(consumer_api)
api.add_namespace(storage_api)
api.add_namespace(totals_api)
api.add_namespace(events_api)
