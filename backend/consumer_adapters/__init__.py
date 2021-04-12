from .ConstantValueConsumerAdapter import ConstantValueConsumerAdapter
from .FakeControllableConsumerAdapter import FakeControllableConsumerAdapter

CONSUMER_TYPE_MAPPING = {
    'constant': ConstantValueConsumerAdapter,
    'fakeControllable': FakeControllableConsumerAdapter
}
