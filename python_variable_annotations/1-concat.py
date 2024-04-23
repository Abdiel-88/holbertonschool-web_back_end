#!/usr/bin/env python3
"""
This module defines a concat function with type annotations.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenated result of str1 and str2.
    """
    return str1 + str2


if __name__ == "__main__":
    concat_function = __import__('1-concat').concat
    print(concat("egg", "shell") == "eggshell")
    print(concat.__annotations__)
