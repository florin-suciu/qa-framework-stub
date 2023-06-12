import logging
import logging.config
import os


def setup_logging():
    # Get the absolute path to the logging.yaml file
    log_config_path = os.path.join(os.path.dirname(__file__), "../config/logging.yaml")

    # Load the logging configuration from the logging.yaml file
    logging.config.fileConfig(log_config_path)

    # Create a logger
    logger = logging.getLogger(__name__)
    return logger
