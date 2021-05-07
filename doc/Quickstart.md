# Quickstart Guide

This quickstart guide will provide you with a little tutorial on how to install
the OpenEnergize software in your environment.

## Prerequirements

- The Docker engine is installed and running on your system (https://docs.docker.com/get-docker/)
- Docker-Compose is installed (https://docs.docker.com/compose/install/)

## Steps

1. Clone the repository
1. Copy the example config for your own configuration:
   ```
   cp exampleconfig.yaml config.yaml
   ```
1. Modify the config.yaml to match your environment. See the [Configuration Doc](Configuration.md)
   for more information
1. Startup with Docker-compose:
   ```
   docker-compose up
   ```
1. Open your browser and open http://localhost:80 (replace the URL with the address
   of the device if you do not installed it on your local device)
