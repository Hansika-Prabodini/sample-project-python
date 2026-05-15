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
        # Avoid building intermediate list; sum(range(n)) runs at C speed
        return sum(range(n))

    @staticmethod
    def max_list(v: List[int]) -> int:
        """Maximum value in a vector

        Args:
            v (List[int]): Vector of integers

        Returns:
            int: Maximum value in the vector
        """
        # Built-in max() runs at C speed, no need for a manual loop
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
        # Generator avoids building an intermediate list; only multiples of m are summed
        return sum(i for i in range(0, n, m))
