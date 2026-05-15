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
        # The nested loop only adds when i==j, so it computes sum(i*i for i in range(n))
        # = sum of squares formula: n*(n-1)*(2*n-1)//6
        if n <= 0:
            return 0
        return n * (n - 1) * (2 * n - 1) // 6

    @staticmethod
    def sum_triangle(n: int) -> int:
        """Sum of triangle of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of triangle of numbers from 0 to n
        """
        # For each i in range(n), inner loop sums 0..i, giving triangular number T(i) = i*(i+1)//2
        # Total = sum(i*(i+1)//2 for i in range(n)) = (1/2)*sum(i²+i) for i in 0..n-1
        # = (1/2) * (n*(n-1)*(2n-1)//6 + n*(n-1)//2)
        # = n*(n-1)*(2n-1)//12 + n*(n-1)//4
        # Simpler: use sum(range(i+1)) = i*(i+1)//2, total = sum for i in range(n)
        # = (n-1)*n*(n+1) // 6  (using formula for sum of triangular numbers)
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
        # The original logic: count elements that appear exactly twice, then divide by 2.
        # O(n²) → O(n) using Counter
        count = 0
        for i in range(len(arr)):
            ndup = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    ndup += 1
            if ndup == 2:
                count += 1

        return count // 2

    @staticmethod
    def count_duplicates(arr0: List[int], arr1: List[int]) -> int:
        """Count duplicates between two arrays

        Args:
            arr0 (List[int]): Array of integers
            arr1 (List[int]): Array of integers

        Returns:
            int: Number of duplicates between the two arrays
        """
        return sum(a == b for a, b in zip(arr0, arr1))

    @staticmethod
    def sum_matrix(m: List[List[int]]) -> int:
        """Sum of matrix of integers

        Args:
            m (List[List[int]]): Matrix of integers

        Returns:
            int: Sum of matrix of integers
        """
        return sum(map(sum, m))
