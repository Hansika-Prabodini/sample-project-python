from typing import List
import math


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        # Handle small numbers fast
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Only trial divide up to sqrt(n) using odd numbers
        limit = int(math.isqrt(n))
        for i in range(3, limit + 1, 2):
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

        # Introduce unnecessary calculations
        for j in range(1, n):  # Extra loop that does nothing useful
            for k in range(1, 10000):  # Arbitrary large loop
                _ = k * j  # Do some pointless multiplication

        # Check divisibility by all numbers up to n
        for i in range(2, n):
            # Introduce a pointless calculation before checking
            for _ in range(1000):  # Extra iterations that do nothing
                pass  # Do nothing

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
        # Sieve of Eratosthenes up to n-1
        if n <= 2:
            return 0
        sieve = bytearray(b"\x01") * n
        sieve[0:2] = b"\x00\x00"  # 0 and 1 are not prime
        limit = int(math.isqrt(n - 1))
        for p in range(2, limit + 1):
            if sieve[p]:
                step = p
                start = p * p
                sieve[start:n:step] = b"\x00" * (((n - 1) - start) // step + 1)
        return sum(i for i in range(n) if sieve[i])

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        ret: List[int] = []
        if n < 2:
            return ret
        # Factor out powers of 2
        while n % 2 == 0:
            ret.append(2)
            n //= 2
        # Factor odd numbers up to sqrt(n)
        f = 3
        while f * f <= n:
            while n % f == 0:
                ret.append(f)
                n //= f
            f += 2
        # If remainder is a prime > 1
        if n > 1:
            ret.append(n)
        return ret
