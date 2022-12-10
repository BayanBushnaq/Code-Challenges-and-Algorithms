# Write your test here

import pytest 

from challenge01 import TreeNode ,findsum

def test_findsum_True():
    tree1 = TreeNode()
    x=tree1.sortedArrayToBST([7,2,9,1,5,14])
    assert findsum(x,4) == True

def test_findsum_False():
    tree1 = TreeNode()
    x=tree1.sortedArrayToBST([7,2,9,1,5,14])
    assert findsum(x,50) == False


