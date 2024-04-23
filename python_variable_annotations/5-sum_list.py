#!/usr/bin/env python3
"""
This module defines a sum_list function with type annotations.
It calculates the sum of a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all floats in a list.

    Args:
    input_list (List[float]): The list of float numbers to sum.

    Returns:
    float: The total sum of the list elements.
    """
    return sum(input_list)

if __name__ == "__main__":
    sum_list_function = __import__('5-sum_list').sum_list
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print(f"sum_list(floats) returns {floats_sum}", end=" ")
    print(f"which is a {type(floats_sum)}")
