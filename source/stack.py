#!python

from doublylinkedlist import DoublyLinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = DoublyLinkedList()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.peek() is None

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.size

    def push(self, item):
        """Insert the given item on the top of this stack."""
        # TODO: Push given item
        self.list.append(item)
        self.size += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        item = self.list.tail
        if item is not None:
            return item.data
        return item

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError
        item = self.list.tail
        self.list.tail = self.list.tail.prev
        self.size -= 1
        return item.data



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack."""
        # TODO: Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        return self.list[len(self.list)-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""
        # TODO: Remove and return top item, if any

        if self.is_empty():
            raise ValueError
        return self.list.pop()



# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack


def test_init():
    s = Stack()
    print(s.peek() is None)
    print(s.length() == 0)
    print(s.is_empty() is True)

def test_init_with_list():
    s = Stack(['A', 'B', 'C'])
    print(s.peek() == 'C')
    print(s.length() == 3)
    print(s.is_empty() is False)

def test_length():
    s = Stack()
    assert s.length() == 0
    s.push('A')
    assert s.length() == 1
    s.push('B')
    assert s.length() == 2
    s.pop()
    assert s.length() == 1
    s.pop()
    assert s.length() == 0



if __name__ == "__main__":
    test_init()
    test_init_with_list()
