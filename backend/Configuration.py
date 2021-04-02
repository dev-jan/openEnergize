import yaml
from backend.producer_adapters import TYPE_MAPPING

def get_configuration() -> dict:
    print("CONFIG-CALLED")
    config = None
    with open('debugconfig.yaml') as file:
        config = yaml.full_load(file)

    if config:
        # instantiate producer adapters
        for producer in config['producers']:
            producer['adapter'] = TYPE_MAPPING[producer['type']](producer['config'])
        print(config)
    return config
