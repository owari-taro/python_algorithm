import sys
import os
sys.path.append(os.pardir)
sys.path.append("../../")
from chapter5 import linear_search
import pytest



# TODO:rewrite more efficeintly
def test_liear_search():
    tmp = [1, 3, 4]
    actual = linear_search(tmp, 1)
    expected = True
    assert actual == expected
   
    tmp = [1, 3, 4]
    actual = linear_search(tmp, 2)
    expected = False
    assert actual == expected
    
    tmp = []
    actual = linear_search(tmp, 2)
    expected = False
    assert actual == expected
