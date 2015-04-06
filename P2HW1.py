__author__ = 'jeredyang'

"""
Q9 Stack class
"""

class Stack:
    """
    A simple implementation of a FILO stack. item type will be int judging from the test
    """

    def __init__(self):
        """
        Initialize the stack.
        """
        self.list = []

    def __len__(self):
        """
        Return number of items in the stack.
        """
        return len(self.list)

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return str(self.list)

    def push(self, item):
        """
        Push item onto the stack.
        """
        self.list.append(item)
        print str(self.list)

    def pop(self):
        """
        Pop an item off of the stack
        """
        item = self.list.pop(-1)
        print str(self.list)
        return item

    def clear(self):
        """
        Remove all items from the stack.
        """
        self.list = []

# ###########################
#  test code for the stack
# my_stack = Stack()
# my_stack.push(72)
# my_stack.push(59)
# my_stack.push(33)
# my_stack.pop()
# my_stack.push(77)
# my_stack.push(13)
# my_stack.push(22)
# my_stack.push(45)
# my_stack.pop()
# my_stack.pop()
# my_stack.push(22)
# my_stack.push(72)
# my_stack.pop()
# my_stack.push(90)
# my_stack.push(67)
# while len(my_stack) > 4:
#     my_stack.pop()
# my_stack.push(32)
# my_stack.push(14)
# my_stack.pop()
# my_stack.push(65)
# my_stack.push(87)
# my_stack.pop()
# my_stack.pop()
# my_stack.push(34)
# my_stack.push(38)
# my_stack.push(29)
# my_stack.push(87)
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# print my_stack.pop()

"""
Q10 Queue class
"""


class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)

    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(-1)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []

