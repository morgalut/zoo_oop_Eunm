from .logger_config import logger

class Debug:
    _debug_enabled = False

    @staticmethod
    def enable_debug(enabled):
        Debug._debug_enabled = enabled
        if enabled:
            logger.info("Debugging enabled")

    @staticmethod
    def log(message):
        if Debug._debug_enabled:
            logger.debug(message)
        else:
            logger.info(message)
