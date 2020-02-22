
from ..queue import Queue
import sys


def test_push():
    queue = Queue(5)
    assert queue.is_empty() == True
    queue.enqueue(10)
    queue.enqueue(3)
    assert queue.deqeue() == 10


"""
def test_multiply():
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=13)
    expected = FieldElement(num=5, prime=13)
    actual = element1 * element2
    assert expected == actual  # element1*element2
    not_expected = FieldElement(num=3, prime=13)
    assert not_expected != actual
\


"""
