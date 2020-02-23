import pytest
from ..queue import Queue


def test_push():
    size = 5
    queue = Queue(size)
    assert queue.is_empty() == True
    queue.enqueue(10)
    queue.enqueue(3)
    assert queue.deqeue() == 10


def test_exception():
    size = 5
    queue = Queue(size)
    with pytest.raises(Queue.Empty):
        queue.deqeue()

    with pytest.raises(Queue.OverFlow):
        for _ in range(size+1):
            queue.enqueue(3)
