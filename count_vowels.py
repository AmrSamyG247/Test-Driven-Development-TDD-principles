#!/usr/bin/python3
"""Count number of vowels in a String in Python"""


def count_vowels(string):
    num_vowels = 0
    for char in string:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+1
    return num_vowels
