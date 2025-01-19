"""
Lecture 4

Formerly leap.py
"""

def is_leap_year(year):
    """
    Determines whether a given year, as an integer, is a leap year.
    A year is a leap year if the year is divisible by 4.

    Input:
        year (int): a year (A.D.)

    Output (bool): True if year is a leap year, False otherwise.

    Examples:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(2025)
        False
    """
    return year % 4 == 0
