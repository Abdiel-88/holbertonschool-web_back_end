#!/usr/bin/env python3
''' Description: Write a function named index_range that takes two integer
                 arguments page and page_size.

'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Return tuple containing pagination start index and end index. '''
    return ((page_size * (page - 1)), page_size * page)
