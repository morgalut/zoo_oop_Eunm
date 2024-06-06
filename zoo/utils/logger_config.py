import logging

def setup_logger():
    logger = logging.getLogger('zoo_logger')
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('zoo.log')
    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

logger = setup_logger()
