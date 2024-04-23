#!/usr/bin/env python3
"""
This module defines a floor function with type annotations.
It takes a float and returns its floor value as an integer.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float number, which is the largest integer less than
    or equal to the number.

    Args:
    n (float): The float number to find the floor of.

    Returns:
    int: The floor of the number.
    """
    return math.floor(n)


if __name__ == "__main__":
    floor_function = __import__('2-floor').floor
    result = floor(3.14)
    expected = math.floor(3.14)
    print(result == expected)
    print(floor.__annotations__)
    print(f"floor(3.14) returns {result}, which is a {type(result)}")
