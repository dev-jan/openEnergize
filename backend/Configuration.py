import yaml
import os
from .producer_adapters import PRODUCER_TYPE_MAPPING
from .consumer_adapters import CONSUMER_TYPE_MAPPING

config = None

def get_configuration() -> dict:
    global config
    if not config or not os.environ.get('FLASK_ENV', '') == 'development':
        with open('debugconfig.yaml') as file:
            config = yaml.full_load(file)

        if config:
            # instantiate producer adapters
            for producer in config['producers']:
                producer['adapter'] = PRODUCER_TYPE_MAPPING[producer['type']](producer['config'])

            # instantiate consumer adapters
            for consumer in config['consumers']:
                consumer['adapter'] = CONSUMER_TYPE_MAPPING[consumer['type']](consumer['config'])
    return config
