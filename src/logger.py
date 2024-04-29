import logging


class Logger:
    def __init__(self):
        self.my_logger = logging.getLogger(__name__)
        self.my_logger.setLevel(logging.ERROR)

        handler = logging.FileHandler('app_errors.log')
        handler.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.my_logger.addHandler(handler)

    @property
    def logger(self):
        return self.my_logger
