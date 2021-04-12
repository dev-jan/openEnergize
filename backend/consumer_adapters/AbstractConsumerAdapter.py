class AbstractConsumerAdapter:
    STATUS_READY = "READY"
    STATUS_OFFLINE = "OFFLINE"
    STATUS_ONLINE = "ONLINE"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, config: dict):
        self.config = config

    def get_current_energy_consumption(self) -> float:
        """ Returns the current energy consumption """
        pass

    def get_type(self) -> str:
        """ Returns the key of the type of the consumption adapter """
        pass

    def is_controllable(self) -> bool:
        """ Returns if the consumer is controllable via this platform """
        return False

    def get_status(self) -> str:
        """ Returns the status of the consumer device, if its ready to be activated
            or if the activation is currently not possible.
        """
        return self.STATUS_UNKNOWN

    def activate(self):
        """ Activate the device to use power """
        pass
