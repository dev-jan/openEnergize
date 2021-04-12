from .ConstantValueProducerAdapter import ConstantValueProducerAdapter
from .ModbusProducerAdapter import ModbusProducerAdapter

PRODUCER_TYPE_MAPPING = {
    'constant': ConstantValueProducerAdapter,
    'modbus': ModbusProducerAdapter
}
