import logging
import requests
from urllib.parse import urljoin
from .AbstractConsumerAdapter import AbstractConsumerAdapter


class VzugWashingMachineConsumerAdapter(AbstractConsumerAdapter):
    """
    Implementation of a V-ZUG Washing Machine Consumer. The washing machine
    must have the feature "V-ZUG HOME" and must be accessible via Network.
    Also the HH-Firmware Version must be at least 1.1 (can be found in the
    settings of the device).

    For security reason, the washing machine can only be activated if someone
    fill the device and start it with the "start later" option. Only then is the
    device ready to be activated.

    configuration:
      ip: IP Address of the device in the network
    """

    def __init__(self, config):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)

    def get_current_energy_consumption(self) -> float:
        return self.config['value']

    def get_type(self) -> str:
        return 'vzugWashingMachine'

    def is_controllable(self) -> bool:
        return True

    def get_status(self) -> str:
        address = self.config['ip']
        url = urljoin('http://' + address, '/hh?command=getSmartStart')
        response = requests.get(url)
        smartStartActive = response.json()['active']
        if smartStartActive:
            return AbstractConsumerAdapter.STATUS_READY
        else:
            return AbstractConsumerAdapter.STATUS_ONLINE

    def activate(self):
        payload = "{'starttime': 0}"
        address = self.config['ip']
        url = urljoin('http://' + address, '/hh?command=setSmartStart?value=' + payload)
        response = requests.get(url)
        self.logger.info('Activated controllable consumer! response: ' + response.json())
