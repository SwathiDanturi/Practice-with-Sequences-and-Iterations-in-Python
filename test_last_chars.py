"""
Practice with sequences, iteration, and functions.
File: test_last_chars.py
Initial authors: COMP801 instructors
Date: 9/5/2024
Developer: Swathi Danturi
Collaborator(s): Samhitha
"""

from core import last_chars


def test_last_chars_lastchars_od():
    """
    Test for input ['hello', 'world']
    """
    word_list = ['hello', 'world']
    expected = ['o', 'd']
    actual = last_chars(word_list)
    assert actual == expected
