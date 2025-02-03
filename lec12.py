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

def gen_randint(n, low=-5, high=5):
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

def how_many(term, word_counts):
    """
    Look up how many instances of the term are recorded
    in the counts.

    Input:
        term (str): term to look up
        word_counts (list[tuple[str,int]]): list of
            (word, count) pairs
    """
    for word, quantity in word_counts:
        if term == word:
            return quantity

def count_all_words(words):
    """
    Count the number of occurrences of each word in the list

    Input:
        words (list[str]): list of words
    
    Output (dict[str,int]): dictionary that maps a string to
        the number of times it appears in the list
    """
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
    return counts
