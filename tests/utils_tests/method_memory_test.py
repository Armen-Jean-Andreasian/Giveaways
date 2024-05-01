import unittest
from utils.profiling import memory_usage_decorator_factory


class TestMethodMemory(unittest.TestCase):
    @memory_usage_decorator_factory(print_delta=True, return_delta=True)
    def count(self, r):
        for _ in range(r):
            pass

    def test_memory_usage(self):
        a = self.count(r=3000000)
        b = self.count(r=3000000)

        self.assertIsInstance(a, float)
        self.assertIsInstance(b, float)
        self.assertGreaterEqual(a, 0)
        self.assertEqual(b, 0)  # python should cache the result of 'a' within the function scope


if __name__ == '__main__':
    unittest.main()
