from .AbstractConsumerAdapter import AbstractConsumerAdapter


class ConstantValueConsumerAdapter(AbstractConsumerAdapter):
    """
    Implementation of a consumer that returns the same value every time. The
    value is provided as config "value".
    """

    def get_current_energy_consumption(self) -> float:
        return self.config['value']

    def get_type(self) -> str:
        return 'constant'
