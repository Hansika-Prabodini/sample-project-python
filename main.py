from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.algorithms.sort import Sort
from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.sql.query import SqlQuery
from llm_benchmark.datastructures.dslist import DsList
from llm_benchmark.strings.strops import StrOps


def single():
    """
    Demonstrates the functionality of SingleForLoop algorithms.
    """
    print("SingleForLoop")
    print("-------------")

    print(f"sum_range(10): {SingleForLoop.sum_range(10)}")
    print(f"max_list([1, 2, 3]): {SingleForLoop.max_list([1, 2, 3])}")
    print(f"sum_modulus(100, 3): {SingleForLoop.sum_modulus(100, 3)}")
    print()


def double():
    """
    Demonstrates the functionality of DoubleForLoop algorithms.
    """
    print("DoubleForLoop")
    print("-------------")

    print(f"sum_square(10): {DoubleForLoop.sum_square(10)}")
    print(f"sum_triangle(10): {DoubleForLoop.sum_triangle(10)}")
    # Generate a random list for count_pairs
    random_list_for_pairs = GenList.random_list(30, 10)
    print(f"count_pairs({random_list_for_pairs}): {DoubleForLoop.count_pairs(random_list_for_pairs)}")
    # Generate random lists for count_duplicates
    list1_duplicates = GenList.random_list(10, 2)
    list2_duplicates = GenList.random_list(10, 2)
    print(
        f"count_duplicates({list1_duplicates}, {list2_duplicates}): {DoubleForLoop.count_duplicates(list1_duplicates, list2_duplicates)}"
    )
    # Generate a random matrix for sum_matrix
    random_matrix_for_sum = GenList.random_matrix(10, 10)
    print(f"sum_matrix({random_matrix_for_sum}): {DoubleForLoop.sum_matrix(random_matrix_for_sum)}")
    print()

def sql():
    """
    Demonstrates the functionality of SqlQuery operations.
    """
    print("SQL")
    print("---")

    print(f"query_album('Presence'): {SqlQuery.query_album('Presence')}")
    print(f"query_album('Roundabout'): {SqlQuery.query_album('Roundabout')}")
    print()

    print("join_albums()")
    # Assuming join_albums returns a list, print the first element
    join_result = SqlQuery.join_albums()
    if join_result:
        print(join_result[0])
    else:
        print("No results from join_albums()")
    print()

    print("top_invoices()")
    # Assuming top_invoices returns a list or similar iterable
    top_invoices_result = SqlQuery.top_invoices()
    if top_invoices_result:
        print(top_invoices_result)
    else:
        print("No results from top_invoices()")
    print()

def primes():
    """
    Demonstrates the functionality of Primes algorithms.
    """
    print("Primes")
    print("------")

    print(f"is_prime(1700): {Primes.is_prime_ineff(1700)}")
    print(f"sum_primes(210): {Primes.sum_primes(210)}")
    print(f"prime_factors(840): {Primes.prime_factors(840)}")
    print()

def sort():
    """
    Demonstrates the functionality of Sort algorithms.
    """
    print("Sort")
    print("----")

    list_for_sort = [5, 3, 2, 1, 4]
    print(f"sort_list({list_for_sort}): ", end="")
    Sort.sort_list(list_for_sort)
    print(list_for_sort)

    list_for_dutch_flag = [5, 3, 2, 1, 4]
    print(f"dutch_flag_partition({list_for_dutch_flag}, 3): ", end="")
    Sort.dutch_flag_partition(list_for_dutch_flag, 3)
    print(list_for_dutch_flag)

    list_for_max_n = [5, 3, 2, 1, 4]
    print(f"max_n({list_for_max_n}, 3): {Sort.max_n(list_for_max_n, 3)}")
    print()


def dslist():
    """
    Demonstrates the functionality of DsList operations.
    """
    print("DsList")
    print("----")

    test_list = [1, 2, 3, 4, 5]
    print("Original list:", test_list)

    modified_list = DsList.modify_list(test_list)
    print("Modified list:", modified_list)

    search_result = DsList.search_list(test_list, 3)
    print("Search result for 3:", search_result)

    sorted_list = DsList.sort_list(test_list)
    print("Sorted list:", sorted_list)

    reversed_list = DsList.reverse_list(test_list)
    print("Reversed list:", reversed_list)

    rotated_list = DsList.rotate_list(test_list, 2)
    print("Rotated list by 2 positions:", rotated_list)

    merged_list = DsList.merge_lists(test_list, [6, 7, 8])
    print("Merged list with [6, 7, 8]:", merged_list)
    print()

def strops():
    """
    Demonstrates the functionality of StrOps operations.
    """
    print("Strops")
    print("----")

    test_str = "racecar"
    print("Original string:", test_str)

    reversed_str = StrOps.str_reverse(test_str)
    print("Reversed string:", reversed_str)

    is_palindrome = StrOps.palindrome(test_str)
    print("Is palindrome:", is_palindrome)
    print()


def main():
    """
    Main function to run all the demonstrations.
    """
    single()
    double()
    sql()
    primes()
    sort()
    dslist()
    strops()


if __name__ == "__main__":
    main()