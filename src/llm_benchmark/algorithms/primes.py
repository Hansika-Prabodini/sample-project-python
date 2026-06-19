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
    def is_prime_ineff(n: int) -> bool:
        """Check if a number is prime (inefficient baseline)

        This is the intentionally slow implementation used as the inefficient
        baseline in benchmark comparisons. It has O(n * 11000) complexity due to:
        1. Nested loops performing n * 10000 pointless multiplications
        2. 1000 extra no-op iterations per divisibility check
        3. Checking all divisors from 2 to n-1

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False

        # Bottleneck 1: pointless nested multiplications
        for j in range(1, n):
            for k in range(1, 10000):
                _ = k * j

        # Bottleneck 2: extra iterations per divisor check
        for i in range(2, n):
            for _ in range(1000):
                pass
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
        
        # Handle factor 2 separately to optimize for odd factors later
        while n % 2 == 0:
            ret.append(2)
            n = n // 2
        
        # Check odd factors starting from 3
        i = 3
        while i * i <= n:
            while n % i == 0:
                ret.append(i)
                n = n // i
            i += 2
        
        # If n is still greater than 1, it's a prime factor
        if n > 1:
            ret.append(n)
        
        return ret
