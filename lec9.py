"""
Lecture 9

Last class:
    Mapping
    Mutation
    Iteration

Today:
    Tuples
    Strings
"""

counts = [2, 4, 3, 4, 3, 1, 9, 3]

# the usual iteration
for num in counts:
    print(num)

# iterating on index: bad
for i in range(len(counts)):
    print(i, counts[i])

# iterating via enumeration: good
for i, num in enumerate(counts):
    print(i, num, i + 1)

