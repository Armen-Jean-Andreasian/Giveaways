import unittest
from src.logger import Logger


def log_exception_legacy(logger: Logger):
    try:
        a / 0
    except NameError as e:
        logger.logger.error(msg=f"Error in obtaining data: {e}")


def log_exception_extended(logger: Logger):
    try:
        a / 0
    except NameError as e:
        logger.log_exception(msg=f"Error in obtaining data: {e}")


def read_logs():
    with open('app_errors.log') as logs:
        return logs.read()


class TestLogger(unittest.TestCase):
    def test_log_exception_legacy(self):
        logger_instance = Logger()
        log_exception_legacy(logger_instance)
        logs1 = read_logs()
        logger_instance = Logger()
        log_exception_legacy(logger_instance)
        logs2 = read_logs()
        self.assertGreater(len(logs2), len(logs1))

    def test_log_exception_extended(self):
        logger_instance = Logger()
        log_exception_extended(logger_instance)
        logs1 = read_logs()
        logger_instance = Logger()
        log_exception_extended(logger_instance)
        logs2 = read_logs()
        self.assertGreater(len(logs2), len(logs1))


if __name__ == '__main__':
    unittest.main()
