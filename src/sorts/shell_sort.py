#!/usr/bin/env python
from threading import Thread

from src.sorts.operations.math import greater, less
from src.sorts.operations.thread import order_sleep, print_graph


# O(log n * n^2)
def shell_sort(list_to_sort, order="asc", visualization_mode=False):
    """
    Shell sort sorts the given list

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
        thread = Thread(target=run_shell_sort, args=(list_to_sort, order_func, visualization_mode))
        print_graph(list_to_sort, thread.start)
        thread.join()
    else:
        run_shell_sort(list_to_sort, order_func, visualization_mode)
    return list_to_sort, operations


def run_shell_sort(list_to_sort, order_func, visualization_mode):
    """
    Runs the main algorithm of shell sort

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

    range_width = len(list_to_sort)
    # n := range_width
    # n --> n/2 in every iteration until n/2^k is close to 1
    # k is in order log n
    # O(log n)
    while range_width != 0:
        range_width = int(range_width / 2)
        shell_run(list_to_sort, range_width, order_func, visualization_mode)
    return list_to_sort


# O(n^2)
def shell_run(list_to_sort, range_width: int, order_func, visualization_mode):
    """
    Runs a swap process in the given list

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        range_width : int
            The width of the elements verification process
        order_func : function
            Order function to compare the elements
        visualization_mode : bool
            If the shell sort was run as visualization mode
    Returns
    ----------
        None
    """

    first_element = 0
    second_element = first_element + range_width

    # n := len(list_to_sort)
    # w := range_width
    # This loop will be executed as many times as w fits in n
    # O(n)
    while second_element < len(list_to_sort):
        # O(n)
        shell_adjust(list_to_sort, range_width, first_element, second_element, order_func, visualization_mode)
        first_element += 1
        second_element = first_element + range_width


def shell_adjust(list_to_sort, range_width: int, first_element: int, second_element: int, order_func,
                 visualization_mode):
    """
    Verifies the given elements until they are sorted, and makes swaps in the list

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        range_width : int
            The width of the elements verification process
        first_element : int
            First element to compare
        second_element : int
            Second element to compare
        order_func : function
            Order function to compare the elements
        visualization_mode : bool
            If the shell sort was run as visualization mode
    Returns
    ----------
        None
    """

    # O(n)
    while (first_element >= 0
           and order_func(list_to_sort[first_element], list_to_sort[second_element]) == 1):
        list_to_sort[first_element], list_to_sort[second_element] = list_to_sort[second_element], list_to_sort[
            first_element]
        first_element, second_element = first_element - range_width, first_element
        order_sleep(1, visualization_mode)


if __name__ == "__main__":
    print(shell_sort([1, 5, 2, 1, 4, 7, 7, 21, 2, 73, 34, 23, -2, 6, 112, -55], "asc", True))
