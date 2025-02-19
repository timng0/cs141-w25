"""
Lecture 19

Last class:
    Recursion
    What are natural numbers?
    Everything in computer science is secretly recursion

Today:
    Recursion on lists
    Sorting
"""

def strings_lengths(strings, sum_so_far):
    """
    Given a list of strings, produces the sum of lengths of strings in 
    the list.
    
    Input:
        strings (list[str]): List of strings
        sum_so_far (int): sum of lengths of strings seen so far

    Output (int): sum of lengths of strings from strings
    """
    if strings == []:
        return sum_so_far
    else:
        first, *rest = strings
        print(f'strings_lengths({rest}, len({first}) + {sum_so_far}))')
        return strings_lengths(rest, len(first) + sum_so_far) 
    
    total = 0
    for string in strings:
        total = total + len(string)
    return total

def insert(item, lst):
    """
    Insert item into the right place in a sorted list.

    Input:
        item (int): the item
        lst (list[int]): sorted list of integers

    Output (list[int]): a list with item in the right spot
    """
    if lst == []:
        return [item]
    else:
        first, *rest = lst
        if item < first:
            return [item] + lst
        else:
            return [first] + insert(item, rest)


def sort(lst):
    """
    Produce a list with the same numbers but in sorted order.

    Input:
        lst (list[int]): list of integers

    Output (list[int]): the same list but sorted in increasing order
    """
    if lst == []:
        return []
    else:
        first, *rest = lst
        return insert(first, sort(rest))
