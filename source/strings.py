#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    """ O(1) best case, O(n*m) worst case
        n = length of text, m = length of pattern"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # iterate over the text

    if find_index(text, pattern) is None:
        return False

    return True


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    """ O(1) best case, O(n*m) worst case
        n = length of text, m = length of pattern"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern == "":
        return 0

    all_indexes = find_all_indexes(text, pattern)
    if all_indexes == []:
        return None
    else:
        return all_indexes[0]


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    """ O(n) best case, O(n*m) worst case
        n = length of text, m = length of pattern"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    index_list = []                                         # O(1), create list
    if pattern == "":                                       # check if patter is empty string, O(1) because it's an empty string
        for index in range(len(text)):                      # iterate through the whole text, because everything counts
                                                            # as a pattern, 0(n), n = length of text
            index_list.append(index)                        # append index, O(1) in average
        return index_list                                   # return, O(1)

    # index = 0
    for index, char in enumerate(text):                     # iterate through whole text, O(n), n = length of text
        count = 0                                           # create variable, O(1)
        for index2, pattern_char in enumerate(pattern):     # iterate through the pattern, O(m) worst case
            if index + index2 < (len(text)):                # compare a sum O(1) to a length O(1), O(1)
                if text[index+index2] == pattern[index2]:   # check if text index is equal to pattern index, O(1)
                    count += 1                              # add to count, O(1)
                    continue
                else:
                    break
        if count == len(pattern):                           # check if count is the same as pttern length, O(1)
            index_list.append(index)                        # append to index_list, O(1) in average

    return index_list                                       # return list, O(1)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
