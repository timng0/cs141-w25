"""
Lecture 6

Last class:
    Functions
    Control flow
    Conditional statements

Today:
    HW2 due at 6 pm

    Fixed vs arbitrarily large data
    Lists
    Looping
"""

def is_prime(n):
    """
    Determine whether n is a prime number.

    Input:
        n (int): positive number

    Output (bool): True if n is prime, False otherwise
    """
    if n == 1:
        return False
    result = True
    for d in range(2, n):
        if n % d == 0:
            result = False
            break
    return result