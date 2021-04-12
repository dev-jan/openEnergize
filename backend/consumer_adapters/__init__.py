from .ConstantValueConsumerAdapter import ConstantValueConsumerAdapter
from .ModbusConsumerAdapter import ModbusConsumerAdapter
from .FakeControllableConsumerAdapter import FakeControllableConsumerAdapter

CONSUMER_TYPE_MAPPING = {
    'constant': ConstantValueConsumerAdapter,
    'modbus': ModbusConsumerAdapter,
    'fakeControllable': FakeControllableConsumerAdapter
}
