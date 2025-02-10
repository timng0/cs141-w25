"""
Lecture 15

Last class:
    Representing things 
    Abstract data types

Today:
    Classes
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

