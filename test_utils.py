import unittest
from string_utils import get_upper_list
from generator_utils import even_odd_generator

class TestUtils(unittest.TestCase):
    def test_upper_list(self):
        self.assertEqual(get_upper_list("abc"), ["A", "B", "C"])

    def test_generator(self):
        gen = even_odd_generator()
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")

if __name__ == "__main__":
    unittest.main()
