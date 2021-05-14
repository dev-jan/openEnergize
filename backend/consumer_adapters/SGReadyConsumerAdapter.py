import logging
import time
import threading
from pymodbus.client.sync import ModbusTcpClient
from .AbstractConsumerAdapter import AbstractConsumerAdapter


class SGReadyConsumerAdapter(AbstractConsumerAdapter):
    """
    Implementation of a SG Ready (SmartGrid Ready) consumer
    via Modbus. SG Ready is a label that is used in the DACH region
    (Germany, Austria and Switzerland) for heat pumps to get regulated.
    The label says that there must be 2 ports to control the state of
    the heat pump. This can also be called via Modbus. For energy control,
    only one port is interesting which allows to set two different modes:
     0 = Normal Mode
     1 = Mode with more Power consumption
    This adapter will set the "line 1" to the state 1 if there is more
    power than needed. After a configured period of time, the device will
    be set back to normal mode.

    configuration:
      gatewayIP: IP of the Modbus Gateway
      gatewayPort: Port of the Modbus Gateway
      address: Memory Address of the SG Ready input 1
      unit: The Modbus unit address of the consumer
      deactivationTimeout: Time to wait before resetting back to normal mode
    """

    def __init__(self, config):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)

    def get_current_energy_consumption(self) -> float:
        # TODO
        return 0

    def is_controllable(self) -> bool:
        return True

    def get_status(self) -> str:
        client = self.get_modbus_connection()
        result = client.read_holding_registers(
            address=self.config['address'],
            count=1,
            unit=self.config['unit']
        )
        if result.isError():
            return AbstractConsumerAdapter.STATUS_OFFLINE
        status = result.registers[0]
        if status == 0:
            return AbstractConsumerAdapter.STATUS_READY
        else:
            return AbstractConsumerAdapter.STATUS_ONLINE

    def deactivate_after_timeout(self):
        time.sleep(self.config.get('deactivationTimeout', 200))
        client = self.get_modbus_connection()
        result = client.write_register(
            address=self.config['address'],
            value=0,
            unit=self.config['unit']
        )
        if result.isError():
            self.logger.error('Cannot reset SG Ready device back to normal')
        else:
            self.logger.info('SG Ready device is back in normal mode')

    def activate(self):
        client = self.get_modbus_connection()
        result = client.write_register(
            address=self.config['address'],
            value=1,
            unit=self.config['unit']
        )
        if result.isError():
            self.logger.warn(
                'Cannot activate SG-Ready device! config: %s' %
                str(self.config)
            )
        else:
            self.logger.info('Activated SG-Ready Device ' + str(self.config))
            thread = threading.Thread(
                target=lambda: self.deactivate_after_timeout()
            )
            thread.daemon = True
            thread.start()

    def get_modbus_connection(self) -> ModbusTcpClient:
        client = ModbusTcpClient(
            self.config['gatewayIP'],
            port=self.config['gatewayPort']
        )
        client.connect()
        return client
