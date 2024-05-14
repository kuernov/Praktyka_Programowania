"""
This module provides utility functions.
"""


def is_odd(n):
    return n % 2 == 1


def sum_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b


def is_even(n):
    """
    Checks if a number is even.
    """
    return n % 2 == 0


def reverse_string(s):
    """
    Returns the reverse of a string.
    """
    return s[::-1]


def find_max(lst):
    """
    Finds the maximum number in a list.
    Returns None if the list is empty.
    """
    if not lst:
        return None
    return max(lst)

