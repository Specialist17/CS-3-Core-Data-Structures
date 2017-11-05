#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: ??? under what conditions?
        O(n) in any case"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions?
        O(1), when index is 0
        Worst case running time: ??? under what conditions?
        O(n) when index is equal to size"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data
        node = self.head            # O(1), set current node to the head of the linked list
        for x in range(index):      # O(n), n = index, loop until we get to index
            if node is not None:    # O(1), check if node is not None
                node = node.next    # O(1), we set the current node to the next one

        return node.data            # O(1), we found the node, we return the data


    def get_node_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions?
        O(1), when index is 0
        Worst case running time: ??? under what conditions?
        O(n), when index is the same as the size"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data
        node = self.head            # O(1), set current node to the head
        for x in range(index):      # O(n), n = index, iterate until reaching index
            if node is not None:    # O(1), check if node is not None
                node = node.next    # O(1), we set the current node to the next one

        return node                 # O(1), we found the node, we return it


    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions?
        O(1), when index is 0, when the list is empty, or when the index is the same as the size
        Worst case running time: ??? under what conditions?
        O(n), n = index"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it

        new_node = Node(item)                           # O(1), set new_node to the Node we want
        node = self.head                                # O(1), set current node to the head

        if index == 0:                                  # O(1), check if index is 0
            self.prepend(item)                          # O(1), prepend
            return

        if self.is_empty() or index == self.size:       # O(1), is_empty and checking the size are both constant
            # Assign head to new node
            self.append(item)                           # O(1), append is constant
            return

        prev_node = self.get_node_at_index(index - 1)   # O(n), worst case for get_node_at_index,
                                                        # set previous node to to the node at index

        if prev_node.next.next is not None:             # O(1), check that node.next.next is not None
            prev_node.next.next = prev_node.next        # O(1), set that node to the node.next

        prev_node.next = Node(item)                     # O(1), set the previous.next to the new node
        self.size += 1                                  # O(1), add one more to the size


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: ??? under what conditions?
        O(1) in every case"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.size += 1
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions?
        O(1) in every case"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.size += 1
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions?
        O(1) if we're trying to replace the first node
        Worst case running time: ??? under what conditions?
        O(n) if node is at the end of the list"""
        # TODO: Find the node containing the given old_item and replace its

        node = self.head                # O(1), set note to current head

        while node is not None:         # O(n) Worst case: loop while node is not None, and until
                                        # we find the data we're looking for
            if node.data == old_item:   # O(1) check if we found the node with the data
                node.data = new_item    # O(1), set old data to new data
                break

            node = node.next            # O(1), set current node to next node

        if node is None:                # O(1), check if node is None
            raise ValueError            # we didn't find the node, so we raise ValueError

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions?
        O(1) if we're trying to delete the first node
        Worst case running time: ??? under what conditions?
        O(n) if node is at the end of the list"""
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
