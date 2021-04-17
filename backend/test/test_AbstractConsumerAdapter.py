from ..consumer_adapters.AbstractConsumerAdapter import AbstractConsumerAdapter


def test_AbstractConsumerAdapter_init():
    config = {
        'someValue': True
    }
    consumer = AbstractConsumerAdapter(config)
    assert consumer.config['someValue']
