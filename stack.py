class Stack:
    def __init__(self):
        """
        Creates an empty stack.
        """
        self.items = []

    def is_empty(self):
        """
        Determine whether the given stack is empty

        Output: True if stack is empty, False otherwise (bool)
        """
        return self.items == []

    def push(self, item):
        """
        Puts an item on the top of the stack.

        Input:
            item (Any): an item
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the item on the top of the stack and produces it.

        Output: the item on the top of the stack (Any)
        """
        return self.items.pop()
