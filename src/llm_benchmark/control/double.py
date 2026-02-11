from collections import Counter
from typing import List


class DoubleForLoop:
    @staticmethod
    def sum_square(n: int) -> int:
        """Sum of squares of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of squares of numbers from 0 to n
        """
        sum_ = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    sum_ += i * j
        return sum_

    @staticmethod
    def sum_triangle(n: int) -> int:
        """Sum of triangle of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of triangle of numbers from 0 to n
        """
        sum_ = 0
        for i in range(n):
            for j in range(i + 1):
                sum_ += j
        return sum_

    @staticmethod
    def count_pairs(arr: List[int]) -> int:
        """Count distinct values that appear exactly twice.

        Args:
            arr (List[int]): Array of integers

        Returns:
            int: Number of distinct values that appear exactly twice

        Raises:
            TypeError: If input is None or not iterable
            ValueError: If input contains non-hashable types

        Examples:
            [1, 1, 2] -> 1 (value 1 appears exactly twice)
            [1, 1, 2, 2] -> 2 (values 1 and 2 each appear exactly twice)
            [] -> 0 (empty list)
        """
        # Input validation
        if arr is None:
            raise TypeError("Input cannot be None")
        
        # Handle empty list
        if len(arr) == 0:
            return 0
        
        # Build frequency map
        try:
            freq = Counter(arr)
        except TypeError:
            raise TypeError("Input contains non-hashable types")
        
        # Count values with frequency exactly equal to 2
        return sum(1 for value, count in freq.items() if count == 2)

    @staticmethod
    def count_duplicates(arr0: List[int], arr1: List[int]) -> int:
        """Count duplicates between two arrays

        Args:
            arr0 (List[int]): Array of integers
            arr1 (List[int]): Array of integers

        Returns:
            int: Number of duplicates between the two arrays
        """
        return len(set(arr0) & set(arr1))

    @staticmethod
    def sum_matrix(m: List[List[int]]) -> int:
        """Sum of matrix of integers

        Args:
            m (List[List[int]]): Matrix of integers

        Returns:
            int: Sum of matrix of integers
        """
        sum_ = 0
        for i in range(len(m)):
            for j in range(len(m[i])):
                sum_ += m[i][j]
        return sum_
