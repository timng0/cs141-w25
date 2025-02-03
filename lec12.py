"""
Lecture 12

Last class:
    Function details
        Scope
        The call stack
        Parameters

Today:
    Tying up parameters and scope
    Dictionaries
"""
import random

def gen_randint(n, low, high):
    """
    Given integers n, low, and high, produces a list of n random
    integers between low and high.

    Input:
        n (int): number of integers to generate, should be positive
        low (int): lower bound
        high (int): upper bound, should be greater than low

    Output: list of n integers between low and high (list[int])
    """
    numbers = []
    for i in range(n):
        numbers.append(random.randint(low, high))
    return numbers
