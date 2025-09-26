import logging

def get_logger():
    logger = logging.getLogger("nop_logger")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("reports/test.log")
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
