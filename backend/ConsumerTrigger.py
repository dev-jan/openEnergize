import time
import threading
import os
import logging

logger = logging.getLogger(__name__)

def get_interval(config: dict) -> int:
    return config.get('check_every', 120)

def start_checking(config: dict):
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        thread = threading.Thread(target=lambda: check_if_consumer_trigger_is_needed(config))
        thread.daemon = True
        thread.start()
        logger.info(f'Start checking to activate consumers if needed every {get_interval(config)} seconds')

def check_if_consumer_trigger_is_needed(config: dict):
    while True:
        time.sleep(get_interval(config))
        total_consumption = sum(float(c['adapter'].get_current_energy_consumption()) for c in config['consumers'])
        total_production = sum(float(p['adapter'].get_current_energy_production()) for p in config['producers'])
        energy_sum = total_production - total_consumption
        logger.debug(f'Current energy sum: {energy_sum}')
        if energy_sum > config['activation_threshold']:
            logger.debug(f'Production capacity ({energy_sum}) is greater than the threshold')
            controllable_and_ready_consumer = next(c for c in config['consumers'] if c['adapter'].is_controllable() and c['adapter'].get_status() == 'READY')
            if controllable_and_ready_consumer:
                controllable_and_ready_consumer['adapter'].activate()
                logger.info(f'activated consumer {controllable_and_ready_consumer}')
            else:
                logger.warn('No controllable consumer found, do nothing...')
