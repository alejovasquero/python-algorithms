import datetime

from src.sorts.heap_sort import heap_sort
from src.sorts.operations.math import get_random_list
from src.sorts.radix_sort import radix_sort
from src.sorts.shell_sort import shell_sort


def take_algorithm_time(array, sorting_algorithm):
    """
    Calculates the time taken for the algorithm to sort the array. The result is in microseconds

    Parameters
    ----------
        array : list
            The array for sorting
        sorting_algorithm : function
            Sorting algorithm to test
    Returns
    ----------
        list : int
            The median taken for the algorithm to sort the array (microseconds)
    """

    start_time = datetime.datetime.now()
    sorting_algorithm(array.copy())
    end_time = datetime.datetime.now() - start_time
    return end_time.microseconds


def take_median_time_for_algorithm(samples, sorting_algorithm):
    """
    Returns the median time for the sorting algorithm given

    Parameters
    ----------
        samples : list[list]
            The arrays for sorting
        sorting_algorithm : function
            Sorting algorithm to test
    Returns
    ----------
        list : int
            The median taken for the algorithm to sort the samples set
    """

    times = []
    for item in samples:
        times.append(take_algorithm_time(item, sorting_algorithm))
    times.sort()
    return times[len(times) // 2]


def get_sorting_data(samples):
    """
    Returns the sorting time for a sample of arrays

    Parameters
    ----------
        samples : list[list]
            The array for sorting
    Returns
    ----------
        list : list
            A list with the time taken for heap_sort, shell_sort, radix_sort and the python sorted_sort
    """

    return [
        take_median_time_for_algorithm(samples, heap_sort),
        take_median_time_for_algorithm(samples, shell_sort),
        take_median_time_for_algorithm(samples, radix_sort),
        take_median_time_for_algorithm(samples, sorted_algorithm)
    ]


def sorted_algorithm(array):
    """
    Returns the sorted array with the python sorted algorithm (Timsort)

    Parameters
    ----------
        array : list
            The array for sorting
    Returns
    ----------
        list : list
            A sorted version of array
    """
    return sorted(array)


def get_sorting_times(sample_size, length, max_value=10000000):
    """
    Returns the time median time for the sorting algorithms with the defined parameters

    Parameters
    ----------
        sample_size : int
            The number of arrays to sort
        length : int
            The length of every array on the sample
        max_value : bool
            The maximum value for sorting
    Returns
    ----------
        list : list
            A list with the time taken for heap_sort, shell_sort, radix_sort and the python sorted_sort
    """

    sample_data = []
    for i in range(sample_size):
        sample_data.append(get_random_list(length, max_value))
    return get_sorting_data(sample_data)
