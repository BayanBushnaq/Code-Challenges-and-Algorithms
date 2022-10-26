# Write your test here

import pytest

from challenge03 import Linkedlist , LinkedListNode

def test_remove_nth_node():
    ''' This method responsible to assert that remove nth method that return a certun node in the linkedlist'''
    ll=Linkedlist()
    

    node1=LinkedListNode(2)
    ll.insert(node1)
    

    node2 = LinkedListNode(55)
    ll.insert(node2)
  
    

    node3 = LinkedListNode(44)
    ll.insert(node3)
  
    node4 = LinkedListNode(66)
    ll.insert(node4)
     
    assert ll.printLinkedList() =="2 => 55 => 44 => 66 => None"
    ll.remove_nth_node(4)
    assert ll.printLinkedList() == "55 => 44 => 66 => None"