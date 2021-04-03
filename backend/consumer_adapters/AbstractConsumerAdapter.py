class AbstractConsumerAdapter:
    def __init__(self, config: dict):
        self.config = config

    def get_current_energy_consumption(self) -> float:
        """ Returns the current energy consumption """
        pass

    def get_type(self) -> str:
        """ Returns the key of the type of the consumption adapter """
        pass
