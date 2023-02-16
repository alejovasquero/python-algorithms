import unittest
from random import randint

from src.sorts.heap_sort import heap_sort
from src.sorts.operations.math import get_random_list


class RandomDataTest(unittest.TestCase):

    def test_should_return_random_data(self):
        values = get_random_list(100, 1000)
        self.assertEqual(100, len(values))
        for i in values:
            self.assertTrue(i<1000)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomDataTest))