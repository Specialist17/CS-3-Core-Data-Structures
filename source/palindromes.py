#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters is string.ascii_uppercase + string.ascii_lowercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

    if text == "":
        return True

    left = 0
    right = len(text) - 1

    while left <= right:
        left_letter = text[left] in string.ascii_letters
        right_letter = text[right] in string.ascii_letters
        print(text[left].lower(), text[right].lower())
        print(left_letter, right_letter)
        print(left, right)
        if left_letter and right_letter:
            if text[left].lower() == text[right].lower():
                left += 1
                right -= 1
            else:
                return False
        elif not left_letter:
            left += 1
        elif not right_letter:
            right -= 1

        else:
            return False

    return True

    # if text == "":
    #     return True
    #
    # text_list = []
    # count = 0
    #
    #
    # # O(n*k) time
    # for char in text:   # O(n) time, where n is length of text
    #     if char in string.ascii_letters:  # O(k) time, where k is length of string.ascii_letters
    #     # if contains(string.ascii_letters, char)
    #         text_list.append(char)  # O(1), on average
    #
    # print(text_list)
    #
    # for characters in zip(reversed(text_list), text_list):
    #     print(characters)
    #
    #     if characters[0].lower() == characters[1].lower():
    #         count += 1
    #     else:
    #         continue
    #
    #
    # if count == len(text_list):
    #     return True
    #
    # return False


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    if left is None and right is None:
        left = 0
        right = len(text) - 1

    if left >= right:
        return True

    left_letter = text[left] in string.ascii_letters
    right_letter = text[right] in string.ascii_letters

    if left_letter and right_letter:
        if text[left].lower() == text[right].lower():
            return is_palindrome_recursive(text, left + 1, right - 1)
        else:
            return False
    elif not left_letter:
        left = left + 1
        return is_palindrome_recursive(text, left, right)
    elif not right_letter:
        right = right - 1
        return is_palindrome_recursive(text, left, right)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    is_palindrome_iterative("Race Fast Safe Car")
