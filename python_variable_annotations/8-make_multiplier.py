#!/usr/bin/env python3
"""
This module defines a make_multiplier function with type annotations.
It creates a multiplier function that
multiplies any float by a specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by a given multiplier.

    Args:
    multiplier (float): The multiplier to apply in the returned function.

    Returns:
    Callable[[float], float]: A function that takes
    a float and multiplies it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function


if __name__ == "__main__":
    # This part is just for your local testing and will not usually be included
    # in the submission file.
    make_multiplier_function = __import__('8-make_multiplier').make_multiplier
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print(f"{fun(2.22)}")
