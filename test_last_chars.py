"""
Practice with sequences, iteration, and functions.
File: test_last_chars.py
Initial authors: COMP801 instructors
Date: 9/5/2024
Developer: Swathi Danturi
Collaborator(s): Samhitha
"""

from core import last_chars


def test_last_chars_lastchars_o_d():
    """
    Test for input ['hello', 'world']
    """
    word_list = ['hello', 'world']
    expected = ['o', 'd']
    actual = last_chars(word_list)
    assert actual == expected


def test_last_chars_lastchars_d_g_e():
    """
    Test for input ['Integrated', 'Computing', 'Practice']
    """
    word_list = ['Integrated', 'Computing', 'Practice']
    expected = ['d', 'g', 'e']
    actual = last_chars(word_list)
    assert actual == expected
