"""
Practice with sequences, iteration, and functions.
File: test_div_nums.py
Initial authors: COMP801 instructors
Date: 9/5/2024
Developer: Swathi Danturi
Collaborator(s): Samhitha
"""

from core import div_nums


def test_nums_2_3_10_term_3():
    """
    Test for input [2, 3, 10] and 3.
    """
    nums = [2, 3, 10]
    term = 3
    expected = [0, 1, 3]
    actual = div_nums(nums, term)
    assert actual == expected


def test_nums_2_3_4_5_6_term_2():
    """
    Test for input [2, 3, 4, 5, 6] and 2.
    """
    nums = [2, 3, 4, 5, 6]
    term = 2
    expected = [1, 1, 2, 2, 3]
    actual = div_nums(nums, term)
    assert actual == expected