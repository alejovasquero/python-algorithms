import unittest
from random import randint

from src.sorts.radix_sort import radix_sort


class RadixSortTest(unittest.TestCase):

    def test_should_sort_two_elements_asc(self):
        list_to_sort = [6, 11]
        sorted_list = radix_sort(list_to_sort.copy())[0]

        self.assertEqual(list_to_sort, sorted_list)

        list_to_sort = [7, 6]
        sorted_list = radix_sort(list_to_sort.copy())[0]
        self.assertEqual(sorted(list_to_sort), sorted_list)

    def test_should_sort_asc_bulk(self):
        list_to_sort = [randint(1, 2000) for i in range(0, 100)]
        sorted_list = radix_sort(list_to_sort.copy())[0]
        self.assertEqual(sorted(list_to_sort), sorted_list)

        list_to_sort = [randint(1, 2000) for i in range(0, 100)]
        sorted_list = radix_sort(list_to_sort.copy())[0]
        self.assertEqual(sorted(list_to_sort), sorted_list)

        list_to_sort = [randint(1, 2000) for i in range(0, 100)]
        sorted_list = radix_sort(list_to_sort.copy())[0]
        self.assertEqual(sorted(list_to_sort), sorted_list)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RadixSortTest))
