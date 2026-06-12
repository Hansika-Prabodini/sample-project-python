from typing import List


def search_list(v: List[int], n: int) -> List[int]:
    """Search a list for a value, returning a list
    of indices where the value is found

    Args:
        v (List[int]): List of integers
        n (int): Value to search for

    Returns:
        List[int]: List of indices where the value is found
    """
    ret = []
    for i in range(len(v)):
        if v[i] == n:
            ret.append(i)
    return ret


def sort_list(v: List[int]) -> List[int]:
    """Sort a list of integers, returns a copy

    Args:
        v (List[int]): List of integers

    Returns:
        List[int]: Sorted list of integers
    """
    ret = v.copy()
    for i in range(len(ret)):
        for j in range(i + 1, len(ret)):
            if ret[i] > ret[j]:
                ret[i], ret[j] = ret[j], ret[i]

    return ret
