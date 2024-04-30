#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Fetch a page of dataset handling deletions."""
        # Validate index range
        if index is not None:
            assert isinstance(index, int), "Index must be an integer"
            assert 0 <= index < len(self.__indexed_dataset), \
                   "Index out of range"

        if index is None:
            index = 0

        dataset = self.indexed_dataset()
        current_index = index
        items_returned = 0
        data = []

        # Collect items until page is full or dataset is exhausted
        while items_returned < page_size and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
                items_returned += 1
            current_index += 1

        next_index = current_index if current_index < len(dataset) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
