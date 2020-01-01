import sys
import os
sys.path.append(os.pardir)
sys.path.append("../../")
import pytest
from chapter4 import merge_arrays



# TODO:rewrite more efficeintly
def test_sort():
    left = [1, 3, 4]
    right = [2, 5, 8]
    actual = merge_arrays(left, right)
    expected = [1, 2, 3, 4, 5, 8]
    assert actual == expected

    left = []
    right = [1, 2, 3]
    actual = merge_arrays(left, right)
    expected = [1, 2, 3]
    assert actual == expected

    left = [1, 2, 3]
    right = []
    actual = merge_arrays(left, right)
    expected = [1, 2, 3]
    assert actual == expected

    left = [1]
    right = [3]
    actual = merge_arrays(left, right)
    expected = [1, 3]
    assert actual == expected
