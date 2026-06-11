from typing import List


def modify_list(v: List[int]) -> List[int]:
    """Modify a list by adding 1 to each element

    Args:
        v (List[int]): List of integers

    Returns:
        List[int]: Modified list of integers
    """
    ret = []
    for i in range(len(v)):
        ret.append(v[i] + 1)
    return ret


def reverse_list(v: List[int]) -> List[int]:
    """Reverse a list of integers, returns a copy

    Args:
        v (List[int]): List of integers

    Returns:
        List[int]: Reversed list of integers
    """
    ret = []
    for i in range(len(v)):
        ret.append(v[len(v) - 1 - i])
    return ret


def rotate_list(v: List[int], n: int) -> List[int]:
    """Rotate a list of integers by n positions

    Args:
        v (List[int]): List of integers
        n (int): Number of positions to rotate

    Returns:
        List[int]: Rotated list of integers
    """
    if len(v) == 0:
        return []
    n = n % len(v)
    ret = []
    for i in range(n, len(v)):
        ret.append(v[i])
    for i in range(n):
        ret.append(v[i])
    return ret


def merge_lists(v1: List[int], v2: List[int]) -> List[int]:
    """Merge two lists of integers, returns a copy

    Args:
        v1 (List[int]): First list of integers
        v2 (List[int]): Second list of integers

    Returns:
        List[int]: Merged list of integers
    """
    ret = []
    for i in range(len(v1)):
        ret.append(v1[i])
    for i in range(len(v2)):
        ret.append(v2[i])
    return ret
