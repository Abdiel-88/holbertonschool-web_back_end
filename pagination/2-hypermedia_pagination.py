#!/usr/bin/env python3
"""
Hypermedia pagination script using a server class to manage data from a CSV
file with additional pagination details.
"""

import csv
import math
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate indices for pagination based on page number and page size."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names with
    hypermedia controls."""
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
        assert isinstance(page, int) and page > 0, \
               "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
               "page_size must be a positive integer"
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Optional[any]]:
        """Return a page of the dataset with hypermedia metadata."""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None if page >= total_pages else page + 1
        prev_page = None if page <= 1 else page - 1

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }