import requests
import xml.etree.ElementTree as et
from urllib.parse import urljoin
from .AbstractStorageAdapter import AbstractStorageAdapter


class VartaBatteryStorageAdapter(AbstractStorageAdapter):
    """
    Implementation of the storage that returns the energy level of a VARTA
    battery (see https://www.varta-ag.com/en/consumer/product-categories/energy-storage-systems).
    """

    def get_current_storage_capacity(self) -> float:
        battery_ip = self.config['battery_ip']
        response = requests.get(urljoin('http://' + battery_ip, '/cgi/ems_data.xml'))
        tree = et.fromstring(response.content)
        value = tree.find("./inverter/var[@name='SOC']").attrib['value']
        return value

    def get_type(self) -> str:
        return 'vartabattery'
