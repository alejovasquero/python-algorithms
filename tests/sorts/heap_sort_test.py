import unittest
from random import randint

from src.sorts.heap_sort import heap_sort


class HeapSortTest(unittest.TestCase):

    def test_should_sort_two_elements_asc(self):
        list_to_sort = [6, 11]
        sorted_list = heap_sort(list_to_sort)

        self.assertEqual(list_to_sort, sorted_list)

        list_to_sort = [-10, -11]
        sorted_list = heap_sort(list_to_sort)
        self.assertEqual(sorted(list_to_sort), sorted_list)

    def test_should_sort_two_elements_desc(self):
        list_to_sort = [6, 11]
        sorted_list = heap_sort(list_to_sort, "desc")

        self.assertEqual(sorted(list_to_sort, reverse=True), sorted_list)

        list_to_sort = [-11, -10]
        sorted_list = heap_sort(list_to_sort, "desc")
        self.assertEqual(sorted(list_to_sort, reverse=True), sorted_list)

    def test_should_sort_asc_bulk(self):
        list_to_sort = [randint(1, 2000) for i in range(0,100)]
        sorted_list = heap_sort(list_to_sort)
        self.assertEqual(sorted(list_to_sort), sorted_list)

        list_to_sort = [randint(1, 2000) for i in range(0,100)]
        sorted_list = heap_sort(list_to_sort)
        self.assertEqual(sorted(list_to_sort), sorted_list)

        list_to_sort = [randint(1, 2000) for i in range(0,100)]
        sorted_list = heap_sort(list_to_sort)
        self.assertEqual(sorted(list_to_sort), sorted_list)

    def test_should_sort_desc_bulk(self):
        list_to_sort = [randint(1, 2000) for i in range(0,1000)]
        sorted_list = heap_sort(list_to_sort, "desc")
        self.assertEqual(sorted(list_to_sort, reverse=True), sorted_list)

        list_to_sort = [randint(1, 2000) for i in range(0,1000)]
        sorted_list = heap_sort(list_to_sort, "desc")
        self.assertEqual(sorted(list_to_sort, reverse=True), sorted_list)

        list_to_sort = [randint(1, 2000) for i in range(0,1000)]
        sorted_list = heap_sort(list_to_sort, "desc")
        self.assertEqual(sorted(list_to_sort, reverse=True), sorted_list)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(HeapSortTest))