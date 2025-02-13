class Stack:
    """
    A collection of items with controlled last in, first out access.
    """
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.__items = []

    def is_empty(self):
        """
        Determine whether the given stack is empty

        Output: True if stack is empty, False otherwise (bool)
        """
        return self.__items == []

    def push(self, item):
        """
        Puts an item on the top of this stack.

        Input:
            item (Any): an item
        """
        self.__items.append(item)

    def pop(self):
        """
        Removes the item on the top of this stack and produces it.

        Output: the item on the top of the stack (Any)
        """
        return self.__items.pop()

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f'Stack: {self.__items}'

    def __str__(self):
        vals = []
        for item in self.__items:
            vals.append(str(item))
        return f'Stack: {", ".join(vals)} (Top)'

    def __eq__(self, other):
        return self.__items == other.__items