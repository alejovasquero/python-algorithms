from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep


def order_sleep(sec, visualization_mode):
    if visualization_mode:
        sleep(sec)


def print_graph(list_to_sort, init_func):
    """
    Makes a graphic of the algorithm process

    Parameters
    ----------
        list_to_sort : list
            List for sorting
        init_func : function
            Initial function for the graphic
    Returns
    ----------
        None
    """

    figure = plt.figure()
    figure.suptitle('Radix Sort', fontsize=16)
    ax = figure.add_subplot(1, 1, 1)
    positions = [i for i in range(len(list_to_sort))]
    bars = ax.bar(positions, list_to_sort, color="green")
    ax.bar_label(bars)

    def func(frame):
        ax.clear()
        bar = ax.bar(positions, list_to_sort, color="green")
        ax.bar_label(bar)
        return bars

    animation = FuncAnimation(figure, func, interval=1000,
                              repeat=True, init_func=init_func)
    plt.tight_layout()
    plt.show()