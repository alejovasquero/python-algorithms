from threading import Thread

from src.sorts.operations.math import greater, less
from src.sorts.operations.thread import order_sleep, print_graph


# O (n log n) + O (n log n) = O (n log n)
def heap_sort(list_to_sort, order="asc", visualization_mode=False):
    """
    Heap sort sorts the given list

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        order : str
            Sorting order. asc or desc. asc is default
        visualization_mode : Boolean
            If the sort will be displayed with graphication of the sorting process
            In visualization mode, the sorting process will be performed in a secondary thread
    Returns
    ----------
        list : list
            A reference of list_to_sort, already ordered
    """

    if order == "asc":
        order_func = greater
    elif order == "desc":
        order_func = less
    else:
        raise ValueError(f"Order not valid: {order}")
    operations = 0
    if visualization_mode:
        thread = Thread(target=run_main_sort, args=(list_to_sort, order_func, visualization_mode))
        print_graph(list_to_sort, thread.start)
        thread.join()
    else:
        operations = run_main_sort(list_to_sort, order_func, visualization_mode)
    return list_to_sort, operations


def run_main_sort(list_to_sort, order_func, visualization_mode):
    """
    Runs the main algorithm of heap sort

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        order_func : function
            Sorting function for comparisons
        visualization_mode : Boolean
            If the sort will be displayed with graphication of the sorting process
    Returns
    ----------
        list : list
            A reference of list_to_sort, already ordered
    """

    operations = 2
    length = len(list_to_sort)

    # O (n log n)
    # O(n)
    for i in range(int(length / 2) - 1, -1, -1):
        operations += heapify(list_to_sort, i, length, order_func, visualization_mode)

        # O(log n)
        operations += 3
    operations += 2

    # O (n log n)
    # O (n)
    for i in range(length - 1, -1, -1):
        list_to_sort[i], list_to_sort[0] = list_to_sort[0], list_to_sort[i]
        order_sleep
        operations += 3

        # O (logn)
        operations += heapify(list_to_sort, 0, i, order_func, visualization_mode)

    return operations


# Heapify has n elements to verify(limit value)
# For every step, n--> n/2, until n/2^k have passed, being k the number of executions
# so k is log2 n
# heapify = O(log n)
def heapify(array_to_heapify, index, limit, order_func, visualization_mode):
    """
    Runs a heapify process in the list from the index element until the limit element

    Parameters
    ----------
        array_to_heapify : list
            List for sorting
        index : int
            Element to make heapify from
        limit : int
            Limit element to run the heapify process
        order_func : function
            Order function to compare the elements
        visualization_mode : bool
            If the heap sort was run as visualization mode
    Returns
    ----------
        operations: int
            The number of elemental operations performed in the heapify process
    """

    index += 1
    right_children = index * 2 + 1
    left_children = index * 2

    max_index = index

    operations = 7

    # first comparison + 3 comparing operations + 2 indexes and subtractions
    operations += 2 + 3 + 4
    if (left_children - 1 < limit and
            order_func(array_to_heapify[left_children - 1], array_to_heapify[max_index - 1]) == 1):
        operations += 1
        max_index = left_children

    # first comparison + 3 comparing operations + 2 indexes and subtractions
    operations += 2 + 3 + 4
    if (right_children - 1 < limit and
            order_func(array_to_heapify[right_children - 1], array_to_heapify[max_index - 1]) == 1):
        operations += 1
        max_index = right_children

    operations += 1
    if max_index != index:
        array_to_heapify[max_index - 1], array_to_heapify[index - 1] = array_to_heapify[index - 1], array_to_heapify[
            max_index - 1]
        order_sleep(1, visualization_mode)
        operations += 9
        operations += heapify(array_to_heapify, max_index - 1, limit, order_func, visualization_mode)

    return operations


if __name__ == "__main__":
    print(heap_sort([1, 5, 2, 1, 4, 7, 7, 21, 2, 73, 34, 23, -2, 6, 112, -55], "asc", True))
