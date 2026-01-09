from typing import List


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_prime_ineff(n: int) -> bool:
        """Check if a number is prime (optimized version)

        This function has been optimized from an inefficient O(n * 11000) implementation
        to an efficient O(sqrt(n)) implementation by:
        1. Removing unnecessary nested loops
        2. Only checking divisibility up to sqrt(n)
        3. Skipping even numbers after checking 2

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Only check odd divisors up to sqrt(n)
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        
        return True


    @staticmethod
    def sum_primes(n: int) -> int:
        """Sum of primes from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of primes from 0 to n
        """
        sum_ = 0
        for i in range(n):
            if Primes.is_prime(i):
                sum_ += i
        return sum_

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        ret = []
        while n > 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    ret.append(i)
                    n = n // i
                    break
        return ret
