"""
Lecture 24

Last class:
    Generative recursion
        Binary search
    Files

Today:
    Pass/fail
    Something I forgot to mention about binary search
    Exceptions
"""

def binary_search(lst, item):
    if lst == []:
        return False
    else:
        mid = len(lst) // 2
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            return binary_search(lst[:mid], item)
        else:
            return binary_search(lst[mid+1:], item)











































def foo(x, y):

    raise NotImplementedError("To be completed.")

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
