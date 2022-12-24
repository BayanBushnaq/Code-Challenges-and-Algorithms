# Write your test here

import pytest 

from challenge01 import BinarySearchTree , Node , has_sum


def test_findsum_True(tree1):
   
    assert has_sum(tree1,3) == True

def test_findsum_False(tree1):
    assert has_sum(tree1,4) == False


@pytest.fixture
def tree1():
    tree = BinarySearchTree()
    tree.insert(7)
    tree.insert(2)
    tree.insert(9)
    tree.insert(1)
    tree.insert(5)
    tree.insert(14)
    return tree
    


