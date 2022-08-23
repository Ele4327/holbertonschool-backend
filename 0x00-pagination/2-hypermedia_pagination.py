import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    return((page - 1) * page_size, page * page_size)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int, page_size: int) -> Dict:

        reg_dataset = self.get_page(page, page_size)

        tot_pages_in_dataset = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(reg_dataset),
            'page': page,
            'data': reg_dataset,
            'next_page': page + 1 if (page + 1) <= tot_pages_in_dataset else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': tot_pages_in_dataset
        }
