class AbstractProducerAdapter:
    def __init__(self, config: dict):
        self.config = config

    def get_current_energy_production(self) -> float:
        """ Returns the current energy production """
        pass
