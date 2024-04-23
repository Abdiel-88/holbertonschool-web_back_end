#!/usr/bin/env python3
"""
This module defines an add function with type annotations.
"""

def add(a: float, b: float) -> float:
    """
    Return the sum of two float numbers.

    Args:
    a (float): The first float number.
    b (float): The second float number.

    Returns:
    float: The sum of the numbers.
    """
    return a + b

if __name__ == "__main__":
    # This part is just for your local testing and will not usually be included in the submission file.
    add_function = __import__('0-add').add
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
