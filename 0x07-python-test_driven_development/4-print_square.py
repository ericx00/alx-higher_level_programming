#!/usr/bin/python3
"""
This is the module "4-print_square"
This module take in one function, print_square()
This function takes one parameter used as the size of a square to print using #
"""


def print_square(size):
    """ Function that prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
