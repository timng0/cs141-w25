"""
Lecture 10

Last class:
    Tuples
    Strings

Today:
    Lists of lists
    while loops
"""

def find_zeros(mat):
    """
    Produce a list of locations in the matrix that
    are zero.

    Input:
        mat (list[list]): matrix
    
    Output (list[tuple[int,int]]): list of locations
    """
    zeros = []
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if val == 0:
                zeros.append((i, j))
    return zeros

def gcd(a, b):
    """
    Produce the greatest common divisor of a and b

    Input:
        a (int): nonnegative integer
        b (int): nonnegative integer
    
    Output (int): gcd of a and b
    """
    m = min(a,b)
    g = 1
    for d in range(2, m+1):
        if a % d == 0 and b % d == 0:
            g = d
    return g

def euclid(a, b):
    """
    Produce the greatest common divisor of a and b

    Input:
        a (int): nonnegative integer
        b (int): nonnegative integer, b <= a
    
    Output (int): gcd of a and b
    """
    m = a
    n = b
    while n != 0:
        r = m % n
        m = n
        n = r
    return m