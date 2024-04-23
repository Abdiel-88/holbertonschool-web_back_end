#!/usr/bin/env python3
"""
This module defines a to_str function with type annotations.
It converts a float to its string representation.
"""


def to_str(n: float) -> str:
    """
    Convert a float to a string and return the string.

    Args:
    n (float): The float number to convert.

    Returns:
    str: The string representation of the float.
    """
    return str(n)


if __name__ == "__main__":
    to_str_function = __import__('3-to_str').to_str
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print(f"to_str(3.14) returns {pi_str} which is a {type(pi_str)}")
