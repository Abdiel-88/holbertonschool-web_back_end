#!/usr/bin/env python3
"""
This module defines a to_kv function with type annotations.
It takes a string and an int/float and returns a tuple consisting of the string
and the square of the int/float as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and a number (int or float) into a tuple containing the
    string and the square of the number as a float.

    Args:
    k (str): The string to be placed in the tuple.
    v (Union[int, float]): The number to be squared and converted to float.

    Returns:
    Tuple[str, float]: A tuple containing the string and the squared value.
    """
    return (k, float(v**2))


if __name__ == "__main__":
    # This part is just for your local testing and will not usually be included
    # in the submission file.
    to_kv_function = __import__('7-to_kv').to_kv
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
