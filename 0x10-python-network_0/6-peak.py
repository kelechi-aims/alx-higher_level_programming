#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of integers to search for a peak in.

    Returns:
    - The peak integer found in the list.
    """
    if not list_of_integers:
        return None

    # Define the left and right indices for binary search
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    # The peak is found when left == right
    return list_of_integers[left]
