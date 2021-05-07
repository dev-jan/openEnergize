# Configuration

The configuration is loaded as YAML file into the backend server and is used
to configurate all parameters for the platform.


## Location

The configuration file should be located in the root folder of the Flask app and
named "configuration.yaml". If this is not the case, The full path can be specified
via the environment variable "APP_CONFIG_PATH". The docker-compose.yml file in
this repository already defined the mounting of the config.yaml.


## Structure

The configuration has the following structure:
```
check_every: 60
activation_threshold: 200

producers:
# list of producers

consumers:
# list of consumers

storages:
# list of storages
```

The different elements are described below.


### check_every

Defines the interval (in seconds), of which the platform checks if some
controllable consumers should be activated. Default is 5 minutes (300 seconds).


### activation_threshold

Defines the threshold (in Watt) to activate controllable consumers. The producers
must at least produce more then the threshold amount of energy more than the
consumers use. Default is 100 Watt.


### Producers

List of the energy producers. Every producer can have the following attributes:

* id: Id of the producer (integer)
* name: Name of the producer that is shown in the UI
* type: Type of the producer. The following types are available:
  * 'constant': Return a constant value
  * 'modbus': Return a value for a Modbus Device
* config: Configuration of the producer. For the possible configuration values for each
  producer, see the documentation of the different producers.


### Consumers

List of the consumer devices. Every consumer has the following attributes:

* id: Id of the consumer (integer)
* name: Name of the consumer that is shown in the UI
* type: Type of the consumer. The following types are available:
  * 'constant': Return a constant value
  * 'modbus': Return a value from a Modbus Device
  * 'fakeControllable': Same as the constant provider, but is also controllable (does nothing)
  * 'vzugHome': Controlls a V-ZUG Device (that is equipped with V-ZUG Home)
* config: Configuration of the consumer. For the possible configuration values for each
  consumer, see the documentation of the different consumers.


### Storages

List of the energy storages. Every storage has the following attributes:

* id: Id of the storage (integer)
* name: Name of the storage that is shown in the UI
* type: Type of the storage. The following types are available:
  * 'constant': Return a constant value for the battery percentage
  * 'vartaBattery': Return the battery percentage from a VARTA battery
* config: Configuration of the storage. For the possible configuration values for each
  storage type, see the documentation of the different storage adapters.
