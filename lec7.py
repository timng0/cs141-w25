"""
Lecture 7

Last class:
    Fixed vs arbitrarily large data
    Lists
    Looping
    for loops
    range

Today:
    Primality testing is secretly accumulation
    Short-circuiting with break
    Nested loops
    More on lists
"""

def is_prime(n):
    """
    Determine whether n is a prime number.

    Input:
        n (int): positive number

    Output (bool): True if n is prime, False otherwise
    """
    result = n > 1
    for d in range(2, n):
        if n % d == 0:
            result = False
            break
    return result

scores = [-4, 4, 3, -2, 5, -5, 2, 2]
grocery = ["eggs", "bread", "bread", "eggs", "milk", [3, 4, 4, -5], []]
