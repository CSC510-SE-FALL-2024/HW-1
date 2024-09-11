"""
This module contains test cases for the merge_sort

"""
from hw2_debugging import merge_sort

def test_case1():
    """
    This is to test the base case
    """
    arr = [38, 27, 43, 3, 9, 82, 10]
    expected = [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort(arr) == expected

def test_case2():
    """
    This is to test the empty array 
    """
    arr = []
    expected = []
    assert merge_sort(arr) == expected

def test_case3():
    """
    This is to test the array with repeated numbers
    """
    arr = [5, 1, 5, 3, 8, 5]
    expected = [1, 3, 5, 5, 5, 8]
    assert merge_sort(arr) == expected
