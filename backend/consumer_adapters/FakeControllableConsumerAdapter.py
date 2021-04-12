import logging
from .AbstractConsumerAdapter import AbstractConsumerAdapter

class FakeControllableConsumerAdapter(AbstractConsumerAdapter):
    """
    Implementation of a consumer that returns the same value every time. The
    value is provided as config "value". This adapter also allows to fake an
    action, as it is controllable (but does nothing on activation).
    """

    def __init__(self, config):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)

    def get_current_energy_consumption(self) -> float:
        return self.config['value']

    def get_type(self) -> str:
        return 'fakeControllable'

    def is_controllable(self) -> bool:
        return True

    def get_status(self) -> str:
        return self.config['status']

    def activate(self):
        self.logger.info('Activated controllable consumer!')
