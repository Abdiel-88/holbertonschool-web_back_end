#!/usr/bin/env python3
"""
Module Description: Implements a function named `index_range` which calculates the start and end index
for pagination, given the page number and the size of the page.

This function is designed to handle pagination calculations where page numbers start from 1.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the indices for pagination based on the page number and page size.

    Args:
    page (int): The current page number, starting from 1.
    page_size (int): The number of items each page contains.

    Returns:
    Tuple[int, int]: A tuple containing the start index and the end index for the page.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
