"""
Lecture 5
"""

def is_leap_year(year):
    """
    Determines whether a given year, as an integer, is a leap year.
    A year is a leap year if the year is divisible by 4 and not divisible
    by 100 unless it is divisble by 400.

    Input:
        year (int): a year (A.D.)

    Output (bool): True if year is a leap year, False otherwise.

    Examples:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(2025)
        False
    """
    print("    Start of is_leap_year")
    is_leap = (year % 4 == 0) and (not year % 100 == 0 or year % 400 == 0)
    print("    End of is_leap_year")
    return is_leap
    print("does not get printed")

# All of this is not part of the function because of the indentation
y = 2019
print("Calling is_leap_year(y)...")
z = is_leap_year(y)
print("Returned from is_leap_year(y)...")
print("Value of z is", z)


def is_even(n):
    """
    Determines if n is even or odd
    
    Input:
        n (int): a number
        
    Output (bool): True if n is even, False otherwise
    """
    return n % 2 == 0
