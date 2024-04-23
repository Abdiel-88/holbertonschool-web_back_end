#!/usr/bin/env python3
"""
This module defines a function element_length with type annotations.
It calculates the length of each element in an iterable of sequences.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, each containing
    an item from the input iterable and its length.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences (like list, str, etc.).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples,
    each with a sequence and its length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    # This part is just for your local testing and will not usually be included
    # in the submission file.
    element_length_function = __import__('9-element_length').element_length
    print(element_length.__annotations__)
