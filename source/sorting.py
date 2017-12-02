#!python
from random import randrange
from binarytree import BinarySearchTree

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    for index, item in enumerate(items):
        if index+1 < len(items):
            if item > items[index+1]:
                return False

    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    while not is_sorted(items):
        for index, item in enumerate(items):
            if index+1 < len(items):
                if item > items[index+1]:
                    items[index], items[index+1] = items[index+1], items[index]
    # TODO: Swap adjacent items that are out of order



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    # Traverse through all array elements
    for i in range(len(items)):
        # Find the minimum element in remaining
        # unsorted array
        min_index = i
        for j in range(i+1, len(items)):
            if items[min_index] > items[j]:
                min_index = j

        # Swap the found minimum element with
        # the first element
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    for index in range(1, len(items)):
        current_item = items[index]
        current_position = index - 1


        while current_position >= 0 and items[current_position] > current_item:
            items[current_position + 1] = items[current_position]
            current_position -= 1

        items[current_position + 1] = current_item


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n + m), where n is the size of items 1
        and m is the size of items 2
    TODO: Memory usage: O(n + m) Why and under what conditions?"""
    merged_list = []
    left_index = 0
    right_index = 0

    # Repeat until one list is empty
    while right_index < len(items2) and left_index < len(items1):
        left = items1[left_index]
        right = items2[right_index]
        if left <= right:
            merged_list.append(left)
            left_index += 1
        elif left >= right:
            merged_list.append(right)
            right_index += 1

    # only one these is going to run
    # add remaining items from items1
    for index in range(left_index, len(items1)):
        merged_list.append(items1[index])

    # add remaining items from items2
    for index in range(right_index, len(items2)):
        merged_list.append(items2[index])

    # if items1_index == len(items1):
    #     # merged_list.append(items2[right_index])
    #     # right_index += 1
    #     merged_list.extend(items2[right_index:])
    #     # break
    # elif right_index == len(items2):
    #     # merged_list.append(items1[items1_index])
    #     # items1_index += 1
    #     merged_list.extend(items1[items1_index:])
    #     # break

    return merged_list
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O((n^2)/2) because it divides the work in 2 halves
    TODO: Memory usage: O(2n) = O(n) because we create two halves of the original list to sort
    and then create another list to merge the sorted half lists"""
    pivot = len(items)//2
    left = items[:pivot]
    right = items[pivot:]

    bubble_sort(left)
    bubble_sort(right)

    items[:] = merge(left, right)


def tree_sort(items):
    tree = BinarySearchTree()
    print(items)
    for item in items:
        tree.insert(item)
    sorted_items = tree.items_in_order()
    print(sorted_items)


def partition(items, left, right, pivot):

    # 
    items[pivot], items[right] = items[right], items[pivot]
    store_index = left
    for i in range(left, right):
        if items[i] < items[right]:
            items[i], items[store_index] = items[store_index], items[i]
            store_index += 1
    items[store_index], items[right] = items[right], items[store_index]
    return store_index


def quick_sort(items, left=None, right=None):

    # set left and right to the first and last index respectively
    if left is None:
        left = 0
        right = len(items) - 1

    # when left index is more than the right index, just stop and return the items
    if left >= right:
        return items

    # create a random pivot point
    pivot = randrange(left, right + 1)

    # get the next pivot point after "dividing" the list into greater than and less than pivot parts
    new_pivot = partition(items, left, right, pivot)

    # recursive calls with the new pivot
    quick_sort(items, left, new_pivot - 1)
    quick_sort(items, new_pivot + 1, right)



def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n*log(n)) all the cases
    TODO: Memory usage: O(n*log(n)) all the cases because we have to create new lists every
    time we split lists in half and when we merge them back"""
    # Check if list is so small it's already sorted (base case)
    # Split items list into approximately equal halves
    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order


    if len(items) > 1:
        pivot = int(len(items)/2)

        left = items[:pivot]
        merge_sort(left)
        right = items[pivot:]
        merge_sort(right)
        items[:] = merge(left, right)


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=split_sort_merge, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    print(sort(items))
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
