"""
Lecture 21

Last class:
    Binary search trees

Today:
    Generative recursion
"""

class BinarySearchTree:
    """
    Represents a binary search tree.

    Attributes:
        value (int): the value stored in the node, None if tree is empty
        left (BinarySearchTree | None): left subtree
        right (BinarySearchTree | None): right subtree
    """
    def __init__(self, value=None):
        """
        Constructor for Tree

        Input:
            value (Any): value for the node, None if empty
        """
        self.value = value
        if value is None:
            self.left = None
            self.right = None
        else:
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

    def is_empty(self):
        """
        True if tree is empty, False otherwise
        """
        return self.value is None

    def insert(self, item):
        """
        Inserts an item into the BST.

        Input:
            item (int): item to be inserted
        """
        if self.is_empty():
            self.value = item
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            if item < self.value:
                self.left.insert(item)
            elif item > self.value:
                self.right.insert(item)

    def __contains__(self, item):
        """
        Determines if given item is present in the tree.

        Input:
            item (int): the value to find
        """
        if self.is_empty():
            return False
        else:
            if item == self.value:
                return True
            elif item < self.value:
                return self.left.__contains__(item)
            else:
                return self.right.__contains__(item)

    def __repr__(self):
        """
        Internal representation of tree.
        """
        if self.is_empty():
            return 'BinarySearchTree()'
        else:
            return f'BinarySearchTree({self.value}, {self.left}, {self.right})'
