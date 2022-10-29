# Write your test here
 
import pytest
from challenge01 import Queue

def test_stack_queue_implement_queue():
    MyQueue = Queue()
    MyQueue.push(1) 
    MyQueue.push(2) 
    MyQueue.push(3)
    print(MyQueue.peek())
    print(MyQueue.pop())
    print(MyQueue.empty())

    assert MyQueue.peek() == 2
    assert MyQueue.pop() == 2
    assert MyQueue.empty() == "The Queue is not empty :)"

