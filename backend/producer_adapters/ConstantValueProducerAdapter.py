from .AbstractProducerAdapter import AbstractProducerAdapter

class ConstantValueProducerAdapter(AbstractProducerAdapter):
    """
    Implementation of the producer that returns the same value every time. The
    value is provided as config "value".
    """

    def get_current_energy_production(self) -> float:
        return self.config['value']

    def get_type(self) -> str:
        return "constant"
