from hw2_debugging import merge_sort

def test_case1():
    arr = [38, 27, 43, 3, 9, 82, 10]
    expected = [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort(arr) == expected

def test_case2():
    arr = []
    expected = []
    assert merge_sort(arr) == expected

def test_case3():
    arr = [5, 1, 5, 3, 8, 5]
    expected = [1, 3, 5, 5, 5, 8]
    assert merge_sort(arr) == expected