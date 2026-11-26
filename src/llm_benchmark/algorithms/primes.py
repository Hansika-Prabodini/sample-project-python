from math import isqrt
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
        if n % 2 == 0:
            return n == 2
        for i in range(3, isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_prime_ineff(n: int) -> bool:
        """Check if a number is prime (inefficiently)

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        for i in range(3, isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True


    @staticmethod
    def sum_primes(n: int) -> int:
        """Sum of primes from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of primes from 0 to n
        """
        if n < 3:
            return 0
        # Sieve of Eratosthenes over [0, n)
        sieve = bytearray([1]) * n
        sieve[0] = sieve[1] = 0
        for p in range(2, isqrt(n - 1) + 1):
            if sieve[p]:
                sieve[p * p :: p] = bytes(len(range(p * p, n, p)))
        return sum(i for i, flag in enumerate(sieve) if flag)

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
