#!/usr/bin/env python3
""" Return a Tuple """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    return ((page - 1) * page_size, page * page_size)
