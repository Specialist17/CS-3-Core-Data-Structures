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

    def is_empty(self):
        return self.size == 0

    def contains(self, element):
        """Return True if this Set contains the given element (key), or False."""
        return self.table.contains(element)

    def add(self, element):
        """Add element to this set, if not present already"""
        if not self.contains(element):
            self.table.set(element, 0)
            self.size += 1

    def remove(self, element):
        """Remove the given element, or raise KeyError"""
        self.table.delete(element)
        self.size -= 1

    def union(self, other_set):
        union_set = Set()

        for element in self.table.keys():
            union_set.table.set(element, 0)
        for element in other_set.table.keys():
            union_set.table.set(element, 0)
        return union_set.table.keys()

    # def union(self, other_set):
    #     union_set = Set()
    #     union_set = self.table.keys()[:]
    #     for element in other_set.table.keys():
    #         union_set.append(element)
    #     return union_set

    def intersection(self, other_set):
        intersection_set = Set()

        for element in other_set.table.keys():
            if self.table.contains(element):
                intersection_set.table.set(element, 0)

        return intersection_set.table.keys()

    def difference(self, other_set):
        difference_set = Set()

        for element in self.table.keys():
             if other_set.table.contains(element):
                 difference_set.table.set(element, 0)

        return difference_set.table.keys()

    def is_subset(self, other_set):

        for element in self.table.keys():
            if element in other_set.table.keys():
                continue
            else:
                return False

        return True


def test_set():
    sA = Set(['John', 'Jane', 'Jack', 'Janice'])
    sB = Set(['Jack', 'Sam', 'Susan', 'Janice'])
    engineers = set(['John', 'Jane', 'Jack', 'Janice'])
    programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])

    print("my set", sA.union(sB))
    print("my set", sB.union(sA))
    print("python set", engineers.union(programmers))
    print("python set", programmers.union(engineers))

    # sA = Set(['John', 'Jane', 'Jack', 'Janice'])
    # sB = Set(['Jack', 'Sam', 'Susan', 'Janice'])
    print("my set sA.intersection(sB):", sA.intersection(sB))
    print("my set sB.intersection(sA):", sB.intersection(sA))
    print("python set", engineers.intersection(programmers))
    print("python set", programmers.intersection(engineers))

    sA = Set(['A', 'B', 'C', 'D', 'X'])
    sB = Set(['A', 'B', 'M', 'P', 'Z'])

    print(sA.intersection(sB))
    print(sB.intersection(sA))

if __name__ == "__main__":
    test_set()
