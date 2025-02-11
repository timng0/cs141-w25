"""
Lecture 16

Last class:
    Classes
        attributes
        methods

Today:
    More on classes
        Hiding information
        Dunder methods
        Modelling
"""
from stack import Stack

class Student:
    """
    Representation of a student at a university
    """
    def __init__(self, name, cnetid, ucid):
        """
        Input:
            name (str): full name for the student
        """
        self.name = name
        self.institution = 'University of Chicago'
        self.id_number = ucid
        self.email = cnetid + '@uchicago.edu'

    def get_cnetid(self):
        """
        Retrieve the CNetID for the student

        Output (str): the CNetID
        """
        cnet = self.email.removesuffix('@uchicago.edu')
        return cnet


def matching_brackets(expr):
    """
    Given an expression, determine whether its brackets are closed properly

    Input;
        expr (str): expression

    Output (bool): True if expression has matched brackets
    """
    st = Stack()

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in expr:
        if char in brackets:
            st.push(char)
        elif char in brackets.values():
            if st.is_empty():
                return False
            matching = st.pop()
            if brackets[matching] != char:
                return False
    return st.is_empty()

