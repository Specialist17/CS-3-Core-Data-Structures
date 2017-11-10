#!python

from hashtable import HashTable


class Set(object):

    def __init__(self, elements=None):
        """Initialize this Set with a hash table, add elements if they're available"""
        self.table = HashTable()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.add(item)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}'.format(key) for key in self.table.keys()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this Set"""
        return 'Set({!r})'.format(self.table.keys())

    def contains(self, element):
        """Return True if this Set contains the given element (key), or False."""
        return self.table.contains(element)

    def add(self, element):
        """Add element to this set, if not present already"""
        self.table.set(element, 0)
        self.size += 1

    def remove(self, element):
        """Remove the given element, or raise KeyError"""
        self.table.delete(element)
        self.size -= 1

    def union(self, other_set):
        union_set = Set()
        union_set.table = self.table
        for element in other_set:
            union_set.table.set(element, 0)
        return union_set.keys()

    def intersection(self, other_set):
        intersection_set = Set()

        for element in other_set:
            if self.table.contains(element):
                intersection_set.table.set(element)

        return intersection_set.keys()

    def difference(self, other_set):
        difference_set = Set()

        for element in self.table.keys():
             if element not in other_set:
                 difference_set.table.set(element)

        return difference_set

    def is_subset(self, other_set):

        for element in self.table.keys():
            if element in other_set:
                continue
            else:
                return False

        return True
