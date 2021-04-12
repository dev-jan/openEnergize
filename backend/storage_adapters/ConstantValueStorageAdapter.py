from .AbstractStorageAdapter import AbstractStorageAdapter

class ConstantValueStorageAdapter(AbstractStorageAdapter):
    """
    Implementation of the storage that returns the same value every time. The
    value is provided as config "value".
    """

    def get_current_storage_capacity(self) -> float:
        return self.config['value']

    def get_type(self) -> str:
        return "constant"
