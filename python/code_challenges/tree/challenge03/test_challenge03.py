# Write your test here

import pytest 

from challenge03 import BST , pre_order 

def test_BST():
    Array1 = BST()
    x=Array1.sortedArrayToBST([0,-3,-10,5,9])
    assert (pre_order(x , [])) == [0, -3, -10, 9, 5]


def test_BST2():
    Array2= BST()
    z = Array2.sortedArrayToBST([3,1])
    assert pre_order(z , []) == [3, 1]