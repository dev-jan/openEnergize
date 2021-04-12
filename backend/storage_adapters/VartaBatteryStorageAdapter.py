import requests
import xml.etree.ElementTree as et
from urllib.parse import urljoin
from .AbstractStorageAdapter import AbstractStorageAdapter


class VartaBatteryStorageAdapter(AbstractStorageAdapter):
    """
    Implementation of the storage that returns the energy level of a VARTA
    battery (see https://www.varta-ag.com/).
    """

    def get_current_storage_capacity(self) -> float:
        battery_ip = self.config['battery_ip']
        url = urljoin('http://' + battery_ip, '/cgi/ems_data.xml')
        response = requests.get(url)
        tree = et.fromstring(response.content)
        value = tree.find("./inverter/var[@name='SOC']").attrib['value']
        return value

    def get_type(self) -> str:
        return 'vartabattery'
