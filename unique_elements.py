#!/usr/bin/python3
"""that takes a list of integers test as input and
returns the count of arr elements in the list.
"""


def count_unique_elements(arr):
    distinct = set(arr)
    return len(distinct)
