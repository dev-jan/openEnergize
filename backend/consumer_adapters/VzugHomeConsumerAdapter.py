import logging
import requests
from urllib.parse import urljoin, quote_plus
from .AbstractConsumerAdapter import AbstractConsumerAdapter


class VzugHomeConsumerAdapter(AbstractConsumerAdapter):
    """
    Implementation of a V-ZUG Home Consumer. This could be a Washing machine,
    a Dishwasher or a Tumber. The requirement of the device is, that it
    must have the feature V-ZUG Home and must be accessible via network.
    Also the HH-Firmware Version must be at least 1.1 (can be found in the
    settings of the device).

    For security reason, the washing machine can only be activated if someone
    fill the device and start it with the "start later" option. Only then is
    the device ready to be activated.

    configuration:
      ip: IP Address of the device in the network
    """

    def __init__(self, config):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)

    def get_current_energy_consumption(self) -> float:
        address = self.config['ip']
        url = urljoin('http://' + address, '/hh?command=getEcoInfo')
        try:
            response = requests.get(url)
            if response.ok:
                return response.json()['energy']['program']
        except requests.exceptions.ConnectionError:
            self.logger.warn(
                "Cannot get energy consumption from device! config: " +
                str(self.config)
            )
        except KeyError:
            self.logger.warn("Cannot read energy consumption. JSON was: " + str(response))
        return 0

    def is_controllable(self) -> bool:
        return True

    def get_status(self) -> str:
        address = self.config['ip']
        url = urljoin('http://' + address, '/hh?command=getSmartStart')
        try:
            response = requests.get(url)
            if response.ok:
                smart_start_active = response.json()['active']
                if smart_start_active:
                    return AbstractConsumerAdapter.STATUS_READY
                else:
                    return AbstractConsumerAdapter.STATUS_ONLINE
            else:
                return AbstractConsumerAdapter.STATUS_OFFLINE
        except requests.exceptions.ConnectionError:
            self.logger.warn(
                "Cannot get energy consumption from device! config: " +
                str(self.config)
            )
            return AbstractConsumerAdapter.STATUS_OFFLINE

    def activate(self):
        address = self.config['ip']
        payload = quote_plus('{"starttime": 0}')
        url = urljoin('http://' + address, '/hh?command=setSmartStart&value=' + payload)
        response = requests.get(url)
        self.logger.info('Activated V-ZUG Device! response: ' + str(response.json()))
