"""
Lecture 18

Last class:
    More modeling with classes (Divvy)

Today:
    Recursion
    What are natural numbers?
    Everything in computer science is secretly recursion
"""

def factorial(n):
    """
    Computes the factorial of a given natural number n.

    Input: 
        n (int): a natural number (i.e. n >= 0)

    Output (int): n!
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

    # iterative version that won't run because it comes after returns
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product

def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n-1)

def strings_lengths(strings):
    if strings == []:
        return 0
    else:
        first, *rest = strings
        return len(first) + strings_lengths(rest)

    # iterative version that won't run because it comes after returns
    total = 0
    for string in strings:
        total = total + len(string)
    return total
