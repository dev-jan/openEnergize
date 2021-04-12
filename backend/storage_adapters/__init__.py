from .ConstantValueStorageAdapter import ConstantValueStorageAdapter
from .VartaBatteryStorageAdapter import VartaBatteryStorageAdapter

STORAGE_TYPE_MAPPING = {
    'constant': ConstantValueStorageAdapter,
    'vartaBattery': VartaBatteryStorageAdapter
}
