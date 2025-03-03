"""
Lecture 24

Last class:
    Generative recursion
        Binary search
    Files

Today:
    Pass/fail
    Something I forgot to mention about binary search
    Exceptions
"""

def binary_search(lst, item):
    if lst == []:
        return False
    else:
        mid = len(lst) // 2
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            return binary_search(lst[:mid], item)
        else:
            return binary_search(lst[mid+1:], item)

