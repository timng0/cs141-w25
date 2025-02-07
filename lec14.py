"""
Lecture 14

Last class:
    More on dictionaries
        Complexity
        Sets

Today:
    Representing things 
    Abstract data types
"""
import stack

def matching_brackets(expr):
    """
    Given an expression, determine whether its brackets are closed properly

    Input;
        expr (str): expression

    Output (bool): True if expression has matched brackets
    """
    st = stack.create()

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in expr:
        if char in brackets:
            stack.push(st, char)
        elif char in brackets.values():
            if stack.is_empty(st):
                return False
            matching = stack.pop(st)
            if brackets[matching] != char:
                return False
    return stack.is_empty(st)

colour = (202, 21, 31)

date = (25, 2, 7)

datetime = (2025, 2, 7, 13, 30, 57)

date = {
    "year": 2025,
    "month": 2,
    "day": 7
}

hw1 = {"name": "Homework #1",
       "short_name": "hw1",
       "deadline": (2025, 1, 7),
       "num_submissions": 191}

table = [['name', 'short_name', 'deadline', 'num_submissions'],
         ['Homework #1', 'hw1', (2025, 1, 7), 191]]

