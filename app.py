from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from src.sorts.operations.time import get_sorting_times


def main():
    """
        Runs the graphication process for heap_sort, shell_sort, radix_sort and python_sort
        This graph is a time comparison
    """
    times = [0]
    heap = [0]
    shell = [0]
    radix = [0]
    python = [0]
    figure, axes = plt.subplots(nrows=1, ncols=1, figsize=(1000, 1000))
    axes.plot(times, heap, color="red", label="Heap Sort")
    axes.plot(times, shell, color="gray", label="Shell Sort")
    axes.plot(times, python, color="green", label="Python Sort")
    axes.plot(times, radix, color="blue", label="Radix Sort")
    plt.rcParams["figure.autolayout"] = True
    plt.legend(loc="upper left")

    def init():
        pass

    def func(frame):
        data = get_sorting_times(10, 2000 + frame * 50, 1000)
        print(data)
        times.append(2000 + frame * 50)
        heap.append(data[0])
        shell.append(data[1])
        radix.append(data[2])
        python.append(data[3])
        axes.plot(times, heap, color="red", label="Heap Sort")
        axes.plot(times, shell, color="gray", label="Shell Sort")
        axes.plot(times, python, color="green", label="Python Sort")
        axes.plot(times, radix, color="blue", label="Radix Sort")

    animation = FuncAnimation(figure, func, repeat=True, init_func=init)
    plt.show()


if __name__ == "__main__":
    main()
