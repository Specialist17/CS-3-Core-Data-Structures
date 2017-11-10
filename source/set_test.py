#!python

from hashset import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0
        assert s.table.length() == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        assert s.size == 3
        assert s.table.length() == 3
        assert s.is_empty() is False

    def test_contains(self):
        s = Set(['A', 'B', 'C', 'D', 'X'])
        assert s.contains('C') == True
        assert s.contains('A') == True

        s.add('Y')
        assert s.contains('Y') == True
        assert s.contains('Z') == False

        s.add('Z')
        assert s.contains('Z') == True

        s.remove('Y')
        assert s.contains('Y') == False

    def test_add(self):
        s = Set()
        assert s.size == 0

        s.add('Y')
        assert s.contains('Y') == True
        assert s.size == 1

        s.add('Y')
        assert s.size == 1

        assert s.contains('Z') == False
        s.add('Z')
        assert s.contains('Z') == True
        assert s.size == 2

    def test_remove(self):
        s = Set(['A', 'B', 'C', 'D', 'X'])
        assert s.size == 5

        s.remove('A')
        assert s.contains('A') == False
        assert s.size == 4

        with self.assertRaises(KeyError):
            s.remove('Z')  # item not in set

        assert s.size == 4

        s.remove('B')
        assert s.contains('B') == False
        assert s.size == 3

        s.remove('C')
        assert s.size == 2
        s.remove('D')
        assert s.size == 1
        s.remove('X')
        assert s.size == 0

    def test_union(self):
        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['M', 'N', 'O', 'A', 'P'])
        assert sA.union(sB).sort() == ['A', 'B', 'C', 'D', 'X', 'M', 'N', 'O', 'P'].sort()
        assert sB.union(sA).sort() == ['A', 'B', 'C', 'D', 'X', 'M', 'N', 'O', 'P'].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set()
        assert sA.union(sB).sort() == ['A', 'B', 'C', 'D', 'X'].sort()
        assert sB.union(sA).sort() == ['A', 'B', 'C', 'D', 'X'].sort()

        sA = Set()
        sB = Set()
        assert sA.union(sB) == []
        assert sB.union(sA) == []

    def test_intersection(self):
        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B', 'C', 'D', 'X'])
        assert sA.intersection(sB).sort() == ['A', 'B', 'C', 'D', 'X'].sort()
        assert sB.intersection(sA).sort() == ['A', 'B', 'C', 'D', 'X'].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B', 'M', 'P', 'Z'])
        assert sA.intersection(sB).sort() == ['A', 'B', 'C', 'D', 'X'].sort()
        assert sB.intersection(sA).sort() == ['A', 'B'].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['M', 'N', 'O', 'A', 'P'])
        assert sA.intersection(sB).sort() == ['A'].sort()
        assert sB.intersection(sA).sort() == ['A'].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set()
        assert sA.intersection(sB).sort() == [].sort()
        assert sB.intersection(sA).sort() == [].sort()
        #
        sA = Set()
        sB = Set()
        assert sA.intersection(sB) == []
        assert sB.intersection(sA) == []

    def test_difference(self):
        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B', 'C', 'D', 'X'])
        assert sA.difference(sB).sort() == [].sort()
        assert sB.difference(sA).sort() == [].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B', 'M', 'P', 'Z'])
        assert sA.difference(sB).sort() == ['C', 'D', 'X'].sort()
        assert sB.difference(sA).sort() == ['M', 'P', 'Z'].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['M', 'N', 'O', 'A', 'P'])
        assert sA.difference(sB).sort() == ['D'].sort()
        assert sB.difference(sA).sort() == ['M', 'N', 'O', 'P'].sort()

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set()
        assert sA.difference(sB).sort() == ['A', 'B', 'C', 'D', 'X'].sort()
        assert sB.difference(sA).sort() == [].sort()

        sA = Set()
        sB = Set()
        assert sA.difference(sB) == []
        assert sB.difference(sA) == []

    def test_is_subset(self):
        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B', 'C', 'D', 'X'])
        assert sA.is_subset(sB) == True
        assert sB.is_subset(sA) == True

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B'])
        assert sA.is_subset(sB) == False
        assert sB.is_subset(sA) == True

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set(['A', 'B', 'M'])
        assert sA.is_subset(sB) == False
        assert sB.is_subset(sA) == False

        sA = Set(['A', 'B', 'C', 'D', 'X'])
        sB = Set()
        assert sA.is_subset(sB) == False
        assert sB.is_subset(sA) == True

        sA = Set()
        sB = Set()
        assert sA.is_subset(sB) == True
        assert sB.is_subset(sA) == True


if __name__ == '__main__':
    unittest.main()
