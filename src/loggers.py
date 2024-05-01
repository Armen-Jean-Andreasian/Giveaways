import logging
import traceback


class ExceptionLogger:
    logs_folder = 'logs'

    def __init__(self):
        self.exception_logger = logging.getLogger(__name__)
        self.exception_logger.setLevel(logging.ERROR)

        self.handler = logging.FileHandler(filename='app_errors.log',
                                           mode='a',
                                           encoding='utf-8')
        self.handler.setLevel(logging.ERROR)

        formatter = logging.Formatter(2 * "\n" + '%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)

    @property
    def logger(self):
        return self.exception_logger

    def log_exception(self, msg: str = "Exception occurred", exc_info=True):
        """ Logs an exception with additional information """
        self.exception_logger.addHandler(self.handler)
        self.exception_logger.error(msg, exc_info=exc_info, extra={'traceback': traceback.format_exc()})
        self.handler.close()  # closing the file explicitly
