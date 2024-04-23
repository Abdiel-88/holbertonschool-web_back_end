#!/usr/bin/env python3
"""
This module defines a sum_mixed_list function with type annotations.
It calculates the sum of a list containing both integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list containing both integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
    float: The total sum of the list elements, returned as a float.
    """
    return float(sum(mxd_lst))


if __name__ == "__main__":
    # This part is just for your local testing and will not usually be included
    # in the submission file.
    sum_mixed_list_function = __import__('6-sum_mixed_list').sum_mixed_list
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(sum_mixed_list.__annotations__)
    print(ans == sum(mixed))
    print(f"sum_mixed_list(mixed) returns {ans} which is a {type(ans)}")
