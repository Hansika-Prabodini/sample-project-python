class StrOps:
    @staticmethod
    def str_reverse(s: str) -> str:
        """Reverse a string

        Args:
            s (str): String to reverse

        Returns:
            str: Reversed string
        """
        # Slice reversal avoids O(n²) string concatenation and runs at C speed
        return s[::-1]

    @staticmethod
    def palindrome(s: str) -> bool:
        """Check if a string is a palindrome

        Args:
            s (str): String to check

        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
