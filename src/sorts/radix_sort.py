from threading import Thread

from src.sorts.operations.math import less, greater
from src.sorts.operations.thread import order_sleep, print_graph


def radix_sort(list_to_sort, order="asc", visualization_mode=False):
    """
    Radix sort sorts the given list

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
    else:
        raise ValueError(f"Order not valid: {order}")

    if visualization_mode:
        thread = Thread(target=run_radix_sort, args=(list_to_sort, order_func, visualization_mode))
        print_graph(list_to_sort, thread.start)
        thread.join()
    else:
        run_radix_sort(list_to_sort, order, visualization_mode)
    return list_to_sort, 0


# O(n*k)
# If k == n
# O(n^2)
def run_radix_sort(list_to_sort, order, visualization_mode=False):
    """
    Runs the main algorithm of radix sort

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        order : str
            Sorting order. asc or desc. asc is default
        visualization_mode : Boolean
            If the sort will be displayed with graphication of the sorting process
    Returns
    ----------
        list : list
            A reference of list_to_sort, already ordered
    """
    # n := len(list_to_sort)
    # O(n)
    max_element = max(list_to_sort)
    element_to_check = 0

    # k := maximum length of the elements in the array to sort
    # O(k)
    while max_element // (10 ** element_to_check) > 0:
        # O(n)
        run_counting_sort(list_to_sort, element_to_check, order, visualization_mode)
        element_to_check += 1

    return list_to_sort


# O(n)
def run_counting_sort(list_to_sort, element_to_check, order, visualization_mode):
    """
    Runs counting sort with the given element

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        element_to_check : int
            Element to check in the sorting process.
            For a number of n digits, the element to check will be counting from the units
        order : str
            Sorting order. asc or desc. asc is default
        visualization_mode : bool
            If the sort will be displayed with graphication of the sorting process
    Returns
    ----------
        list : list
            A reference of list_to_sort, already ordered
    """

    length = len(list_to_sort)
    result = [0] * length
    count_array = [0] * 10

    # O(n)
    for i in range(length):
        index = list_to_sort[i] // (10 ** element_to_check)
        count_array[index % 10] += 1

    # O(1)
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    # O(n)
    for i in range(length - 1, -1, -1):
        value = list_to_sort[i] // (10 ** element_to_check)
        result[count_array[value % 10] - 1] = list_to_sort[i]
        count_array[value % 10] -= 1

    # O(n)
    for i in range(length):
        list_to_sort[i] = result[i]
    order_sleep(1, visualization_mode)


if __name__ == "__main__":
    print(radix_sort([122, 4445, 21312, 112321, 4434, 711, 71, 2221, 332, 7300, 344, 223, 24, 26, 112, 55, 1, 0], "asc", True))
