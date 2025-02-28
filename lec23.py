"""
Lecture 23

Last class:
    Generative recursion
        Euclid's algorithm for greatest common divisor
        Merge sort

Today:
    Generative recursion
        Binary search
    Files
"""
import textwrap

def binary_search(lst, item):
    print(lst)
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

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def merge(lst1, lst2):
    """
    Merge two sorted lists into one big list
    """
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        first1, *rest1 = lst1
        first2, *rest2 = lst2
        if first1 < first2:
            return [first1] + merge(rest1, lst2)
        else:
            return [first2] + merge(lst1, rest2)

def sort(lst):
    if lst == []:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        left = sort(lst[:mid])
        right = sort(lst[mid:])
        return merge(left, right)

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

    def __print_r(self, prefix, last, vformat, maxdepth):
        """
        Recursive method to print out the tree. Should not be
        called directly. See print() method for more details
        """
        if maxdepth is not None:
            if maxdepth == 0:
                return
            else:
                maxdepth -= 1    
    
        if len(prefix) > 0:
            if last:
                lprefix1 = prefix[:-3] + u"  └──"
            else:
                lprefix1 = prefix[:-3] + u"  ├──"
        else:
            lprefix1 = u""
    
        if len(prefix) > 0:
            lprefix2 = prefix[:-3] + u"  │"
        else:
            lprefix2 = u""
    
        if last:
            lprefix3 = lprefix2[:-1] + "   "
        else:
            lprefix3 = lprefix2 + "  "
    
        if not self.is_empty():
            ltext = (vformat).format(self.value)
        else:
            ltext = "EMPTY"
    
        ltextlines = textwrap.wrap(ltext, 80, initial_indent=lprefix1, subsequent_indent=lprefix3)
    
        print(lprefix2) 
        print("\n".join(ltextlines))
    
        if self.is_empty():
            return
        else:
            for i, st in enumerate([self.left, self.right]):
                if i == len([self.left, self.right]) - 1:
                    newprefix = prefix + u"   "
                    newlast = True
                else:
                    newprefix = prefix + u"  │"
                    newlast = False

                st.__print_r(newprefix, newlast, vformat, maxdepth)
    
    
    def print(self, vformat="{}", maxdepth=None):
        """
        Prints out the tree.
        
        Parameters:
        - vformat: Format string for the value
        - maxdepth: Maximum depth to print
        """
        self.__print_r(u"", False, vformat, maxdepth)

