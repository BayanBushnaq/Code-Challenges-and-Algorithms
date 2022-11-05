# Write your test here
import pytest

from challenge01 import BinaryTree , pre_order

def test_Tree():
    tree1 = BinaryTree() 
    x = tree1.buildtree([3,9,20,15,7],[9,3,15,20,7])
    assert (pre_order(x , [])) == [3, 9, 20, 15, 7]

def test_Binart_Tree():
    tree2 = BinaryTree() 
    y = tree2.buildtree([-1],[-1])
    assert (pre_order(y , [])) == [-1]