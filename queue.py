def create():
    """
    Creates an empty queue.

    Input:
        None

    Output: empty queue (Queue)
    """
    return []

def is_empty(qu):
    """
    Determines whether the given queue is empty.

    Input:
        qu (Queue): the queue

    Output: True if queue is empty, False otherwise (bool)
    """
    return qu == []

def enqueue(qu, item):
    """
    Adds an item to the back of the queue.

    Input:
        qu (Queue): the queue
        item (Any): a value

    Output: None
    """
    qu.append(item)

def dequeue(qu):
    """
    Removes the item at the front of the queue and produces it.

    Input:
        qu (Queue): the queue

    Output: item at the front of the queue (Any)
    """
    return qu.pop(0)
