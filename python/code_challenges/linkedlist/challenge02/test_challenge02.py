# Write your test here

import pytest
from challenge02 import Linkedlist , LinkedListNode


def test_find_middle():
    ''' this test method ensure return the middle of the LinkedList'''
    ll=Linkedlist()

    node1=LinkedListNode(2)
    ll.insert(node1)

    node2 = LinkedListNode(55)
    ll.insert(node2)

    node3 = LinkedListNode(44)
    ll.insert(node3)

    node4 = LinkedListNode(66)
    ll.insert(node4)

    ll.middleNode()
    print(ll.printLinkedList())

    
    

    assert ll.printLinkedList() =="2 => 55 => 44 => 66 => None"
    assert ll.middleNode() == [44, 66]
    # assert ll.middleNode() == "The middle element is:  44"
    # assert ll.middleNode() == "The rest of LinkedList after middle =>"
    # assert ll.middleNode() == "44"
    # assert ll.middleNode() == "66"

def test_find_middle2():
    ''' this test method ensure return the middle of the LinkedList'''
    llist=Linkedlist()

    node1=LinkedListNode(1)
    llist.insert(node1)

    node2 = LinkedListNode(2)
    llist.insert(node2)

    node3 = LinkedListNode(4)
    llist.insert(node3)

    node4 = LinkedListNode(6)
    llist.insert(node4)

    node5 = LinkedListNode(11)
    llist.insert(node5)

    llist.middleNode()
    print(llist.printLinkedList())

    
    

    assert llist.printLinkedList() =="1 => 2 => 4 => 6 => 11 => None"
    assert llist.middleNode() == [4, 6, 11]
    


    






