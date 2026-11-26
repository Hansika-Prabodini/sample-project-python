from llm_benchmark.generator.gen_list import GenList


def test_random_list_length() -> None:
    assert len(GenList.random_list(25, 10)) == 25


def test_random_list_max_is_exclusive() -> None:
    # With m=1 the only valid value is 0; an inclusive bound would yield 1s too.
    assert set(GenList.random_list(1000, 1)) == {0}


def test_random_list_values_in_range() -> None:
    assert all(0 <= x < 5 for x in GenList.random_list(1000, 5))
