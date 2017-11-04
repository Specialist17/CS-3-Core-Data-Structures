#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # iterate over the text

    # check if the patter is an empty string
    if pattern == "":
        return True

    # iterate through each character in the text
    for index, char in enumerate(text):
        # keep track of a count to 
        count = 0

        #
        for index2, pattern_char in enumerate(pattern):
            if text[index+index2] == pattern[index2]:
                count += 1
            else:
                break
        if count == len(pattern):
            return True

    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern == "":
        return 0

    for index, char in enumerate(text):
        count = 0
        for index2, pattern_char in enumerate(pattern):
            if text[index+index2] == pattern[index2]:
                count += 1
            else:
                break
        if count == len(pattern):
            return index

    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    index_list = []
    if pattern == "":
        for index in range(len(text)):
            index_list.append(index)
        return index_list

    for index, char in enumerate(text):
        count = 0
        for index2, pattern_char in enumerate(pattern):
            if index + index2 < (len(text)):
                print(index2)
                print("text value", text[index+index2], "pattern value", pattern[index2])
                print("text index", index+index2, "pattern index", index2)
                print(text[index+index2] == pattern[index2])
                if text[index+index2] == pattern[index2]:
                    count += 1
                    continue
                else:
                    break
        if count == len(pattern):
            index_list.append(index)

    print("index_list", index_list)

    return index_list


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
