"""
Lecture 21

Last class:
    Trees

Today:
    Binary search trees
"""

class Tree:
    """
    Represents a tree.

    Attributes:
        value (Any): the value stored in the node, None if tree is empty
        children (list[Tree] | None): list of subtrees, None if tree is empty
    """

    def __init__(self, value=None):
        """
        Constructor for Tree

        Input:
            value (Any): value for the node, None if empty
        """
        self.value = value
        if value is None:
            self.children = None
        else:
            self.children = []

    def is_empty(self):
        """
        True if tree is empty, False otherwise
        """
        return (self.value is None and
                self.children is None)

    def add_child(self, tree):
        """
        Adds a subtree to self. Self must be non-empty.

        Input:
            tree (Tree): subtree
        """
        assert not self.is_empty() and isinstance(tree, Tree)
        self.children.append(tree)

    def __len__(self):
        """
        Reports the number of nodes in the tree.
        """
        if self.is_empty():
            return 0
        else:
            count = 1
            for subtree in self.children:
                count = count + subtree.__len__()
            return count

    def __contains__(self, item):
        """
        Determines if given item is present in the tree.

        Input:
            item (Any): the value to find
        """
        if self.is_empty():
            return False
        else:
            if item == self.value:
                return True
            else:
                for subtree in self.children:
                    if subtree.__contains__(item):
                        return True
                return False

    def __repr__(self):
        """
        Internal representation of tree.
        """
        if self.is_empty():
            return 'Tree()'
        else:
            return f'Tree({self.value}, {self.children})'
