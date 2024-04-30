#!/usr/bin/env python3
"""
Simple pagination script using a server class to manage data from a CSV file.
"""

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the indices for pagination based on the page number and page size.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset based on page and page_size."""
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return the appropriate slice of the dataset
        return dataset[start_index:end_index] if start_index < len(dataset) else []