#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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


# O (n log n) + O (n log n) = O (n log n)
def heap_sort(list_to_sort, order="asc", visualization_mode=False):
    if (order == "asc"):
        order_func = greater
    elif (order == "desc"):
        order_func = less
    else:
        raise ValueError(f"Order not valid: {order}")

    if (visualization_mode):
        figure = plt.figure()
        ax = figure.add_subplot(1, 1, 1)
        positions = [i for i in range(len(list_to_sort))]
        bars = ax.bar(positions, list_to_sort)

        def func(frame):
            i = len(list_to_sort) - frame - 1
            heapify(list_to_sort, i, len(list_to_sort), order_func)
            ax.clear()
            print(frame)
            print(ax)
            ax.bar(positions, list_to_sort)
            print(list_to_sort)
            return bars

        animation = FuncAnimation(figure, func, frames=len(list_to_sort), interval=1000, repeat=False)
        plt.show()

    # O (n log n)
    # O(n)
    for i in range(int(len(list_to_sort) / 2) - 1, -1, -1):
        # O(log n)
        heapify(list_to_sort, i, len(list_to_sort), order_func)

    # O (n log n)
    # O (n)
    for i in range(len(list_to_sort) - 1, -1, -1):
        list_to_sort[i], list_to_sort[0] = list_to_sort[0], list_to_sort[i]
        # O (logn)
        heapify(list_to_sort, 0, i, order_func)

    return list_to_sort


# Heapify has n elements to verify(limit value)
# For every step, n--> n/2, until n/2^k have passed, being k the number of executions
# so k is log2 n
# heapify = O(log n)
def heapify(array_to_heapify, index, limit, order_func):
    index += 1
    right_children = index * 2 + 1
    left_children = index * 2

    max_index = index

    if (left_children - 1 < limit and
            order_func(array_to_heapify[left_children - 1], array_to_heapify[max_index - 1]) == 1):
        max_index = left_children

    if (right_children - 1 < limit and
            order_func(array_to_heapify[right_children - 1], array_to_heapify[max_index - 1]) == 1):
        max_index = right_children

    if (max_index != index):
        array_to_heapify[max_index - 1], array_to_heapify[index - 1] = array_to_heapify[index - 1], array_to_heapify[
            max_index - 1]
        heapify(array_to_heapify, max_index - 1, limit, order_func)


if __name__ == "__main__":
    heap_sort([1, 5, 2, 1, 4, 7, 7, 21, 2, 73, 34, 23], "asc", True)