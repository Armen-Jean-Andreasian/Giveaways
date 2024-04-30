import logging
import traceback


class Logger:
    def __init__(self):
        self.my_logger = logging.getLogger(__name__)
        self.my_logger.setLevel(logging.ERROR)

        handler = logging.FileHandler('app_errors.log', mode='a', encoding='utf-8')
        handler.setLevel(logging.ERROR)

        formatter = logging.Formatter(2 * "\n" + '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.my_logger.addHandler(handler)
        handler.close()  # closing the file explicitly

    @property
    def logger(self):
        return self.my_logger

    def log_exception(self, msg: str = "Exception occurred", exc_info=True):
        """ Logs an exception with additional information """
        self.my_logger.error(msg, exc_info=exc_info, extra={'traceback': traceback.format_exc()})
