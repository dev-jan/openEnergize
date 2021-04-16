from .ConstantValueConsumerAdapter import ConstantValueConsumerAdapter
from .ModbusConsumerAdapter import ModbusConsumerAdapter
from .FakeControllableConsumerAdapter import FakeControllableConsumerAdapter
from .VzugWashingMachineConsumerAdapter import VzugWashingMachineConsumerAdapter

CONSUMER_TYPE_MAPPING = {
    'constant': ConstantValueConsumerAdapter,
    'modbus': ModbusConsumerAdapter,
    'vzugWashingMachine': VzugWashingMachineConsumerAdapter,
    'fakeControllable': FakeControllableConsumerAdapter
}
