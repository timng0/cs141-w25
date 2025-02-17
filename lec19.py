"""
Lecture 18

Last class:
    Recursion
    What are natural numbers?
    Everything in computer science is secretly recursion

Today:
    Recursion on lists
    Sorting
"""

def strings_lengths(strings):
    """
    Given a list of strings, produces the sum of lengths of strings in 
    the list.
    
    Input:
        strings (list[str]): List of strings

    Output (int): sum of lengths of strings from strings
    """
    if strings == []:
        return 0
    else:
        first, *rest = strings
        return len(first) + strings_lengths(rest)
