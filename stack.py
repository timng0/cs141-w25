def create():
    """
    Creates an empty stack.

    Input:
        None

    Output: empty stack (Stack)
    """
    return []

def is_empty(st):
    """
    Determine whether the given stack is empty
    Input:
        st (Stack): the stack

    Output: True if stack is empty, False otherwise (bool)
    """
    return st == []

def push(st, item):
    """
    Puts an item on the top of the stack.

    Input:
        st (Stack): the stack
        item (Any): an item

    Output: None
    """
    st.append(item)

def pop(st):
    """
    Removes the item on the top of the stack and produces it.

    Input:
        st (Stack): the stack

    Output: the item on the top of the stack (Any)
    """
    return st.pop()
