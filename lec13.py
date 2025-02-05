"""
Lecture 13

Last class:
    Tying up parameters and scope
    Dictionaries

Today:
    Midterm information
    More on dictionaries
        Complexity
        Sets
        Structures
"""

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
