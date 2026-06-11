from llm_benchmark.datastructures.list_query import search_list, sort_list
from llm_benchmark.datastructures.list_transform import (
    merge_lists,
    modify_list,
    reverse_list,
    rotate_list,
)


class DsList:
    modify_list = staticmethod(modify_list)
    search_list = staticmethod(search_list)
    sort_list = staticmethod(sort_list)
    reverse_list = staticmethod(reverse_list)
    rotate_list = staticmethod(rotate_list)
    merge_lists = staticmethod(merge_lists)
