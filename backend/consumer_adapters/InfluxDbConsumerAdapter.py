import logging
import requests
from urllib.parse import urljoin, quote_plus
from .AbstractConsumerAdapter import AbstractConsumerAdapter


class InfluxDbConsumerAdapter(AbstractConsumerAdapter):
    """
    This Adapter will fetch the latest value from an InfluxDB. InfluxDB
    is a time based database that is often used to save timeseries.

    configuration:
      url: Address of the influxDB (example: https://localhost:8086)
      attribute: Full name of the attribute to fetch (including DB/RP name)
      column: Name of the column to fetch
    """

    def __init__(self, config):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)

    def get_current_energy_consumption(self) -> float:
        address = self.config['url']
        query = f"""SELECT last("{self.config['column']}") FROM
                {self.config['attribute']}
                WHERE time > now() - 4h GROUP BY * ORDER BY DESC LIMIT 1"""
        url = urljoin(address, '/query?q=' + quote_plus(query))
        try:
            response = requests.get(url)
            if not response.ok:
                raise requests.exceptions.ConnectionError('invalid response!')

            return response.json()['results'][0]['series'][0]['values'][0][1]
        except requests.exceptions.ConnectionError:
            self.logger.warn(
                'Cannot get energy consumption from device! config: ' +
                str(self.config)
            )
        except KeyError:
            self.logger.warn(
                'Cannot get consumption, response was: ' +
                str(response.json())
            )
        return 0
