from random import randint


def less(a, b):
    """
    Return a value to check if a < b

    Parameters
    ----------
        a : int
            Integer a
        b : int
            Integer b
    Returns
    ----------
        value : int
            1 (a<b), -1 (a>b), 0 if a=b
    """

    if a < b:
        return 1
    elif a > b:
        return -1
    return 0


def greater(a, b):
    """
    Return a value to check if a > b

    Parameters
    ----------
        a : int
            Integer a
        b : int
            Integer b
    Returns
    ----------
        value : int
            1 (a>b), -1 (a<b), 0 if a=b
    """

    if a > b:
        return 1
    elif a < b:
        return -1
    return 0


def get_random_list(size, limit=10000000):
    """
    Returns a random list of values

    Parameters
    ----------
        size : int
            Size of the array
        limit : int
            Maximum value to be returned
    Returns
    ----------
        value : list
            List of random number, with size given
    """

    answer = []
    while len(answer) < size:
        answer.append(randint(0, limit))
    return answer
