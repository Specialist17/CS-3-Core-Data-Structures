#!python

from doublylinkedlist import DoublyLinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = DoublyLinkedList()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running Time and why
        O(1) every case, because we keep track of the tail at all times, and enqueue appends at the tail"""
        # TODO: Insert given item
        self.list.append(item)             # set tail to the Node(item), constant time
        self.size += 1

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running Time and why
        O(1), because we keep track of the head at all times and dequeue removes at the head"""
        # TODO: Remove and return front item, if any

        if self.is_empty():
            raise ValueError("Head is empty, can't dequeue")

        head = self.list.head.data
        self.list.head = self.list.head.next
        self.size -= 1
        return head


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running Time and why
        O(1) in average, becase when appending at the end of array we sometimes
        have to reallocate the entire list when Appending, but it's a relatively rare case"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running Time and why
        O(n) all cases, we have to shift all elements every time we remove something from
        the beginning of the array"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError

        return self.list.pop(0)


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
