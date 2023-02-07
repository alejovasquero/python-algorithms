#!/usr/bin/env python
# coding: utf-8

# In[31]:


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


def shell_sort(list_to_sort, order="asc", visualization_mode = False):
    if(order=="asc"):
        order_func = greater
    elif(order=="desc"):
        order_func = less
    else:
        raise ValueError(f"Order not valid: {order}")
    
    
    range_width = len(list_to_sort)
    while range_width!=0:
        range_width = int(range_width/2)
        shell_run(list_to_sort, range_width, order_func)
    return list_to_sort
        
def shell_run(list_to_sort, range_width: int, order_func):
    for i in range(0, len(list_to_sort)):
        first_element = i
        second_element = i + range_width
        shell_adjust(list_to_sort, range_width, first_element, second_element, order_func)

            
def shell_adjust(list_to_sort, range_width:int, first_element: int, second_element: int, order_func):
    while(first_element>=0 
          and second_element<len(list_to_sort) 
          and order_func(list_to_sort[first_element], list_to_sort[second_element]) == 1):
        print(f"Moving elements {list_to_sort[first_element]} {list_to_sort[second_element]}")
        list_to_sort[first_element], list_to_sort[second_element] = list_to_sort[second_element], list_to_sort[first_element]
        first_element, second_element = first_element - range_width, first_element


# In[32]:

