#!python

import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return None
    if item == array[index]:
        return index
    else:
        # index += 1
        # return linear_search_recursive(array, item, index)
        return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    # length = (len(array)/2) + (len(array)%2)
    #
    # while length > 0:
    #     print("1. length before iteration: ",length)
    #     print("2. item we are looking for: ", item)
    #     print("3. current item: ", array[length - 1])
    #     if item == array[length - 1]:
    #         return length - 1
    #
    #     if item > array[length]:
    #         array = array[length:]
    #         print('4. when item is greater: ', array)
    #     else:
    #         array = array[:length]
    #         print('4. when item is smaller: ', array)
    #     length = (len(array)/2) + (len(array)%2)
    #     print("5. length after iteration: ", len(array))
    #
    # return None

    # Jeff's solution
    lower_index = 0
    upper_index = len(array) - 1

    while lower_index <= upper_index:
        middle_index = (lower_index + upper_index) // 2

        if array[middle_index] == item:
            return middle_index
        elif array[middle_index] > item:
            upper_index = middle_index - 1
        elif array[middle_index] < item:
            lower_index = middle_index + 1

    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    # _____________ Second Attempt (after iterative being discussed in class) _____________
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    middle = (left + right) / 2
    if left <= right:

        if array[middle] == item:
            return middle
        elif item < array[middle]:
            right = middle - 1
            return binary_search_recursive(array, item, left, right)
        elif item > array[middle]:
            left = middle + 1
            return binary_search_recursive(array, item, left, right)


    #  _____________ First Attempt _____________
    # right = len(array) - 1
    # if item == array[len(array)/2]:
    #     return len(array)/2
    #
    # if right and left:
    #     if item == array[right]:
    #         return right
    #     elif item > array[right]:
    #         left = (right + left)/2
    #         return binary_search_recursive(array, item, left, right)
    #     else:
    #         right = (right + left)/2
    #         return binary_search_recursive(array, item, left, right)
    # else:
    #     if item > array[right]:
    #         left = (len(array) - 1)/2
    #         right = len(array) - 1
    #         return binary_search_recursive(array, item, left, right)
    #     else:
    #         right = (len(array) - 1)/2
    #         left = 0
    #         return binary_search_recursive(array, item, left, right)


    return None
