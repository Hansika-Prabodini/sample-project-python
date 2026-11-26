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
        n = index(n)  # same TypeError as range() for non-integers
        if n <= 0:
            return 0
        return (n - 1) * n * (2 * n - 1) // 6

    @staticmethod
    def sum_triangle(n: int) -> int:
        """Sum of triangle of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of triangle of numbers from 0 to n
        """
        n = index(n)
        if n <= 0:
            return 0
        return (n - 1) * n * (n + 1) // 6

    @staticmethod
    def count_pairs(arr: List[int]) -> int:
        """Count pairs of numbers in an array

        A pair is defined as exactly two numbers in the array that are equal.

        Args:
            arr (List[int]): Array of integers

        Returns:
            int: Number of pairs in the array
        """
        # Each value occurring exactly twice contributed 2 then got halved.
        return sum(1 for c in Counter(arr).values() if c == 2)

    @staticmethod
    def count_duplicates(arr0: List[int], arr1: List[int]) -> int:
        """Count duplicates between two arrays

        Args:
            arr0 (List[int]): Array of integers
            arr1 (List[int]): Array of integers

        Returns:
            int: Number of duplicates between the two arrays
        """
        # Only equal positions (i == j) were ever compared.
        return sum(1 for a, b in zip(arr0, arr1) if a == b)

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
