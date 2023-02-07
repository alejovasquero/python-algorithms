import unittest
from random import randint

from src.sorts.heap.heap import Heap


def less(a, b):
    if (a < b):
        return 1
    elif (a > b):
        return -1
    return 0


def greater(a, b):
    if (a > b):
        return 1
    elif a < b:
        return -1
    return 0


class HeapTest(unittest.TestCase):

    def test_should_create_heap_with_size(self):
        heap = Heap(14)
        self.assertEqual(14, len(heap.list_data) - 1)

        heap = Heap(10)
        self.assertEqual(10, len(heap.list_data) - 1)

        heap = Heap(25)
        self.assertEqual(25, len(heap.list_data) - 1)

        heap = Heap(1000)
        self.assertEqual(1000, len(heap.list_data) - 1)

    def test_maintain_min_heap_invariant(self):
        heap = Heap(25, less)
        for i in range(0, 25):
            heap.push_element(randint(0, 1000))
        self.assert_min_heap_invariant(heap)

        heap = Heap(25, less)
        heap.push_element(1000)
        heap.push_element(1)
        self.assert_min_heap_invariant(heap)

        heap = Heap(1000, less)
        for i in range(0, 1000):
            heap.push_element(randint(0, 1000))
        self.assert_min_heap_invariant(heap)

    def test_maintain_max_heap_invariant(self):
        heap = Heap(25, greater)
        for i in range(0, 25):
            heap.push_element(randint(0, 1000))
        self.assert_max_heap_invariant(heap)

        heap = Heap(25, greater)
        heap.push_element(1000)
        heap.push_element(1)
        self.assert_max_heap_invariant(heap)

        heap = Heap(1000, greater)
        for i in range(0, 1000):
            heap.push_element(randint(0, 1000))
        self.assert_max_heap_invariant(heap)

    def assert_min_heap_invariant(self, heap: Heap):
        heap_list = heap.list_data

        for i in range(1, len(heap_list)):
            if (heap_list[i] != None):
                if (2 * i < len(heap_list) and heap_list[2 * i] != None):
                    self.assertTrue(heap_list[i] <= heap_list[2 * i])
                if (2 * i + 1 < len(heap_list) and heap_list[2 * i + 1] != None):
                    self.assertTrue(heap_list[i] <= heap_list[2 * i + 1])

    def assert_max_heap_invariant(self, heap: Heap):
        heap_list = heap.list_data

        for i in range(1, len(heap_list)):
            if (heap_list[i] != None):
                if (2 * i < len(heap_list) and heap_list[2 * i] != None):
                    self.assertTrue(heap_list[i] >= heap_list[2 * i])
                if (2 * i + 1 < len(heap_list) and heap_list[2 * i + 1] != None):
                    self.assertTrue(heap_list[i] >= heap_list[2 * i + 1])


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(HeapTest))
