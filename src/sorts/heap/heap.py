from collections import deque
from math import inf
import random


# In[9]:


class Heap:
    list_data: deque
    current_size: int
    max_size: int
    comparator_func = None

    def __init__(self, size: int = 10, comparator_func = None):
        if(size<=0):
            raise ValueError(f"Invalid length {size}")
        self.list_data = deque([], size+1)
        for i in range(0, size+1):
            self.list_data.append(None)
        self.current_size = 0
        self.max_size = size

        if comparator_func == None:
            self.comparator_func = less
        else:
            self.comparator_func = comparator_func

    def push_element(self, element: int):
        if(self.current_size == self.max_size):
            raise ValueError("Heap Full")
        self.current_size+=1
        self.list_data[self.current_size] = element
        current_pointer = self.current_size

        movement_flag = current_pointer+1
        while movement_flag!=current_pointer and current_pointer!=1:
            movement_flag = current_pointer
            parent = int(current_pointer/2)
            if(self.comparator_func(self.list_data[current_pointer], self.list_data[parent]) == 1):
                temp = self.list_data[current_pointer]
                self.list_data[current_pointer] = self.list_data[parent]
                self.list_data[parent] = temp
                current_pointer = parent


def less(a,b):
    if(a<b):
        return 1
    elif (a>b):
        return -1
    return 0


def greater(a, b):
    if(a>b):
        return 1
    elif a<b:
        return -1
    return 0