# Write your test here
import pytest
from classLinkedList import Linkedlist , LinkedListNode
from challenge01 import deletegivenNode

def test_linkedlist():
    ll=Linkedlist()

    node1=LinkedListNode(2)
    ll.insert(node1)

    node2 = LinkedListNode(55)
    ll.insert(node2)

    node3 = LinkedListNode(44)
    ll.insert(node3)

    deletegivenNode(node2)

    assert ll.printLinkedList() =="2 => 44 => None"



