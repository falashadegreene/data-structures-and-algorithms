import pytest
from code_challenges.insertion_sort import insertion_sort


def test_insertion_sort():
    list = [6, 2, 1, 3, 4]
    actual = insertion_sort(list)
    expected = [1, 2, 3, 4, 6]
    assert actual == expected


def test_second_insertion_sort():
    list = [2, 17, 5, -1]
    actual = insertion_sort(list)
    expected = [-1, 2, 5, 17]
    assert actual == expected
