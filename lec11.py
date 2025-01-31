"""
Lecture 11

Last class:
    Lists of lists
    while loops

Today:
    Function details
        Scope
        The call stack
        Parameters
"""

def incr(a):
    """
    Increases a number by one.

    Input:
        a (int): a number

    Output (int): number, incremented by one
    """
    one = 1
    return a + one

def plus(m, n):
    """
    Applies plus to m and n.

    Input:
        m (int): an integer
        n (int): an integer

    Output (int): the integer m plus n
    """
    ans = add(m)
    return ans

def add(a):
    """
    Adds a to n.

    Input: 
        a (int): a number

    Output (int): the addition of a and n
    """
    return a + n


def f(i):
    i = i + 1
    return i

def g(i):
    j = h(i * 5)
    return j

def h(i):
    return i + 1

def main():
    i = 7
    j = k = l = 0

    j = f(i)
    k = f(j * 3)
    l = g(i)

    return i, j, k, l

def incr_zeroth(xs):
    """
    Increments the 0th element of the given list.

    Input:
        xs (list): a list

    Output: ?
    """
    xs[0] = xs[0] + 1
