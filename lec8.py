"""
Lecture 8

Last class:
    Primality testing is secretly accumulation
    Short-circuiting with break
    Nested loops
    More on lists

Today:
    Mapping
    Mutation
    Iteration
    Tuples?
"""

strings = ["cat", "", "pepper", "shoe", "paper"]
lengths = []
for string in strings:
    lengths = lengths + [len(string)]

### The "mapping" pattern
<new_list> = []     # initialize empty list
for <item> in <list>:
    # do something with the item to create a new item
    <new_item> = ... <item> ...
    # add new item to list
    <new_list>.append(<new_item>)
