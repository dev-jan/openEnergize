import logging
import operator
from .AbstractProducerAdapter import AbstractProducerAdapter
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from cachetools import cachedmethod, TTLCache


class ModbusProducerAdapter(AbstractProducerAdapter):
    """
    Implementation of a producer that returns the value that is fetched via
    a the MODBUS protocol.

    configuration:
      gatewayIP: IP of the Modbus Gateway
      gatewayPort: Port of the Modbus Gateway
      address: Memory Address to read from the Modbus device
      unit: The Modbus unit to read from
      factor: (optional) Multiply the value with the given factor
    """
    def __init__(self, config: dict):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)
        self.cache = TTLCache(maxsize=100, ttl=60)

    @cachedmethod(operator.attrgetter('cache'))
    def get_current_energy_production(self) -> float:
        for _ in range(10):
            client = ModbusTcpClient(
                self.config['gatewayIP'],
                port=self.config['gatewayPort']
            )
            client.connect()
            address = self.config['address']
            unit = self.config['unit']
            factor = self.config.get('factor', 1)
            result = client.read_holding_registers(
                address=address,
                count=2,
                unit=unit
            )
            client.close()
            if not result.isError():
                registers = result.registers
                decoder = BinaryPayloadDecoder.fromRegisters(
                    registers,
                    Endian.Big,
                    wordorder=Endian.Big
                )
                raw_value = decoder.decode_32bit_int()
                real_value = raw_value * factor
                return real_value
            else:
                self.logger.warn('Cannot read values from modbus, retry...')
        self.logger.error(
            'All retries failed to read values for producer %s' %
            str(self.config)
        )
        return 0
