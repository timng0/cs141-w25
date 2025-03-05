"""
Lecture 25

Last class:
    Hidden binary search costs 
    Exceptions

Today
    Raising exceptions
    Creating exceptions
"""

class MyError(Exception):
    pass

def foo(x, y):
    if y == 0:
        return x / y
    if y == 1:
        return x / u
    d = {}
    x = d["a"]

def bar(y):
    try:
        foo(4, y)
    except ZeroDivisionError:
        print("Tried to divide by zero, caught in bar")
    finally:
        print("Running finally code in bar")
    print("After try block in bar")
    print()

def baz(y):
    try:
        bar(y)
    except NameError as e:
        print("Ran into a name error,", e)
    except ZeroDivisionError:
        print("Tried to divide by zero, caught in baz")
    finally:
        print("Running finally code in baz")
    print("After try block in baz")
