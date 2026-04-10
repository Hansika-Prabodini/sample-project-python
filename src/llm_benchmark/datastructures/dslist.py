import logging
from typing import List

logger = logging.getLogger(__name__)


class DsList:
    @staticmethod
    def modify_list(v: List[int]) -> List[int]:
        """Modify a list by adding 1 to each element

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Modified list of integers
        """
        ret = [x + 1 for x in v]
        return ret

    @staticmethod
    def search_list(v: List[int], n: int) -> List[int]:
        """Search a list for a value, returning a list
        of indices where the value is found

        Args:
            v (List[int]): List of integers
            n (int): Value to search for

        Returns:
            List[int]: List of indices where the value is found
        """
        ret = [i for i, x in enumerate(v) if x == n]
        return ret

    @staticmethod
    def sort_list(v: List[int]) -> List[int]:
        """Sort a list of integers, returns a copy

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Sorted list of integers
        """
        ret = sorted(v)
        return ret

    @staticmethod
    def reverse_list(v: List[int]) -> List[int]:
        """Reverse a list of integers, returns a copy

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Reversed list of integers
        """
        ret = v[::-1]
        return ret

    @staticmethod
    def rotate_list(v: List[int], n: int) -> List[int]:
        """Rotate a list of integers by n positions

        Negative values of ``n`` rotate the list to the left by ``abs(n)``
        positions (equivalent to a right rotation of ``len(v) - abs(n)``
        positions) because ``n`` is normalised via ``n % len(v)``.

        Args:
            v (List[int]): List of integers
            n (int): Number of positions to rotate

        Returns:
            List[int]: Rotated list of integers
        """
        ret = []
        if not v:
            return ret
        n = n % len(v)
        if n == 0:
            return v.copy()
        ret = v[n:] + v[:n]
        return ret

    @staticmethod
    def merge_lists(v1: List[int], v2: List[int]) -> List[int]:
        """Merge two lists of integers, returns a copy

        Args:
            v1 (List[int]): First list of integers
            v2 (List[int]): Second list of integers

        Returns:
            List[int]: Merged list of integers
        """
        ret = []
        ret.extend(v1)
        ret.extend(v2)
        return ret


# Keep module-level aliases for backward compatibility
modify_list = DsList.modify_list
search_list = DsList.search_list
sort_list = DsList.sort_list
reverse_list = DsList.reverse_list
rotate_list = DsList.rotate_list
merge_lists = DsList.merge_lists
