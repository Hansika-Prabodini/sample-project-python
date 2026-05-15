from typing import List


class SingleForLoop:
    @staticmethod
    def sum_range(n: int) -> int:
        """Sum of range of numbers from 0 to n

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of range of numbers from 0 to n
        """
        # O(1) formula: sum of 0..n-1 = n*(n-1)//2
        return n * (n - 1) // 2

    @staticmethod
    def max_list(v: List[int]) -> int:
        """Maximum value in a vector

        Args:
            v (List[int]): Vector of integers

        Returns:
            int: Maximum value in the vector
        """
        return max(v)

    @staticmethod
    def sum_modulus(n: int, m: int) -> int:
        """Sum of modulus of numbers from 0 to n

        Args:
            n (int): Number to sum up to
            m (int): Modulus

        Returns:
            int: Sum of modulus of numbers from 0 to n
        """
        # Sum of multiples of m that are < n: 0, m, 2m, ..., k*m where k = (n-1)//m
        # = m * (0 + 1 + ... + k) = m * k*(k+1)//2
        if m == 0:
            return 0
        k = (n - 1) // m
        return m * k * (k + 1) // 2
