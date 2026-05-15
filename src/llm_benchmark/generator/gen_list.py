import logging
from random import randint
from typing import List

logger = logging.getLogger(__name__)


class GenList:
    @staticmethod
    def random_list(n: int, m: int) -> List[int]:
        """Generate a list of random integers

        Args:
            n (int): Number of integers to generate
            m (int): Maximum value of integers (exclusive)

        Returns:
            List[int]: List of random integers
        """
        if m <= 0:
            raise ValueError(f"m must be > 0, got {m}")
        if n < 0:
            raise ValueError(f"n must be >= 0, got {n}")
        return [randint(0, m - 1) for _ in range(n)]

    @staticmethod
    def random_matrix(n: int, m: int) -> List[List[int]]:
        """Generate a matrix of random integers

        Args:
            n (int): Number of rows
            m (int): Number of columns

        Returns:
            List[List[int]]: Matrix of random integers
        """
        return [GenList.random_list(m, m) for _ in range(n)]
