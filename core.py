"""
Practice with sequences, iteration, and functions.
File: core.py
Initial authors: COMP801 instructors
Date: 9/5/2024
Developer: Swathi Danturi
"""


def div_nums(num_list, term):
    """
    Return a list whose values are from `num_list`, divided by `term`, and
    converted to integers.

    Example: div_nums([2, 3, 10], 3) returns [0, 1, 3]

    Requirements:
    - Apply the accumulation pattern
    - Do not call Python built-in functions or methods.

    :param num_list: list of integers
    :param term: int
    :return: list of integers
    """

    new_list = []
    index = 0
    for num in num_list:
        new_list[index:index] = [num // term]
        index += 1
    return new_list


def last_chars(word_list):
    """
    Return a list of characters that represent the last chararcter of each word
    in `word_list`.

    Example: last_chars(['hello', 'world']) returns ['o', 'd']

    Requirements:
        Apply the accumulation pattern
        Do not call built-in functions and do not use Python library methods

    :param word_list: list of strings
    :return: list of strings
    """

    new_word_list = []
    index = 0
    for each_word in word_list:
        new_word_list[index:index] = each_word[-1]
        index += 1
    return new_word_list
