from ..producer_adapters.AbstractProducerAdapter import AbstractProducerAdapter


def test_AbstractProducerAdapter_init():
    config = {
        'someValue': True
    }
    producer = AbstractProducerAdapter(config)
    assert producer.config['someValue']
