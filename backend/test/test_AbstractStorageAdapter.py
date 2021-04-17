from ..storage_adapters.AbstractStorageAdapter import AbstractStorageAdapter


def test_AbstractStorageAdapter_init():
    config = {
        'someValue': True
    }
    storage = AbstractStorageAdapter(config)
    assert storage.config['someValue']
