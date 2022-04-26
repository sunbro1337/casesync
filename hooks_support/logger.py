import logging.config


# logging.config.fileConfig()
# logging.config.dictConfig()

def create_logger(name, logger_lvl=logging.DEBUG, handler_lvl=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    logger = logging.getLogger(name)
    logger.setLevel(logger_lvl)

    handler = logging.StreamHandler()
    handler.setLevel(handler_lvl)

    formatter = logging.Formatter(format)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
