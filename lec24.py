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

def _binary_search(lst, item, start, end):
    if start >= end:
        return False
    else:
        mid = (start + end) // 2
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            return _binary_search(lst, item, start, mid)
        else:
            return _binary_search(lst, item, mid + 1, end)


def binary_search(lst, item):
    return _binary_search(lst, item, 0, len(lst))
