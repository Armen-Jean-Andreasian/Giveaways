import unittest
from utils.profiling import execution_time_decorator_factory


class TestMethodTimer(unittest.TestCase):
    @execution_time_decorator_factory(print_delta=True, return_delta=True)
    def count(self, r):
        for _ in range(r):
            pass

    def test_execution_time(self):
        a = self.count(r=3000000)
        b = self.count(r=3000000)

        self.assertIsInstance(a, float)
        self.assertIsInstance(b, float)
        self.assertGreater(a, 0)
        self.assertGreater(b, 0)


if __name__ == '__main__':
    unittest.main()

