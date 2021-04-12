class AbstractStorageAdapter:
    def __init__(self, config: dict):
        self.config = config

    def get_current_storage_capacity(self) -> float:
        """ Returns the current storage capacity in percent """
        pass

    def get_type(self) -> str:
        """ Returns the key of the type of the storage adapter """
        pass
