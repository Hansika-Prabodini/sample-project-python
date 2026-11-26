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
        n = index(n)  # same TypeError as range() for non-integers
        if n <= 0:
            return 0
        return n * (n - 1) // 2

    @staticmethod
    def max_list(v: List[int]) -> int:
        """Maximum value in a vector

        Args:
            v (List[int]): Vector of integers

        Returns:
            int: Maximum value in the vector
        """
        v[0]  # keep IndexError on empty input
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
        if type(n) is int and type(m) is int and n > 0 and m > 0:
            # Sum of multiples of m in [0, n): m * (1 + 2 + ... + k)
            k = (n - 1) // m
            return m * k * (k + 1) // 2
        return sum(i for i in range(n) if i % m == 0)
