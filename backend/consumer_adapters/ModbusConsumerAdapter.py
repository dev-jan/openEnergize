from .AbstractConsumerAdapter import AbstractConsumerAdapter
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder

class ModbusConsumerAdapter(AbstractConsumerAdapter):
    """
    Implementation of the consumer that returns the value that is fetched via
    a the MODBUS protocol.
    """

    def __init__(self, config: dict):
        super().__init__(config)
        self.client = ModbusTcpClient(config['gatewayIP'], port=config['gatewayPort'])
        self.client.connect()

    def get_current_energy_consumption(self) -> float:
        address = self.config['address']
        unit = self.config['unit']
        factor = self.config.get('factor', 1)
        result = self.client.read_holding_registers(address=address, count=2, unit=unit)
        registers = result.registers
        decoder = BinaryPayloadDecoder.fromRegisters(registers, Endian.Big, wordorder=Endian.Big)
        rawValue = decoder.decode_32bit_int()
        realValue = rawValue * factor
        return realValue

    def get_type(self) -> str:
        return 'modbus'
