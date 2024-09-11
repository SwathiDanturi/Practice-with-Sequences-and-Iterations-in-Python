"""
Practice with sequences, iteration, and functions.
File: client.py
Initial authors: COMP801 instructors
Date: 9/5/2024
Developer: Swathi Danturi
"""

from core import div_nums, last_chars


def main():
    """
    Demo functionality of core.py functions.
    """
    nums = [2, 3, 10]
    term = 3
    result = div_nums(nums, term)
    print(result)

    word_list = ['hello', 'world']
    result = last_chars(word_list)
    print(result)


if __name__ == "__main__":
    main()
