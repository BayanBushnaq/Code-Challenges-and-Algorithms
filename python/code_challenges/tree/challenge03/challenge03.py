# Write here the code challenge solution

class TreeNode():
    ''' This Main Class responsible to define any given array to Tree'''
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val 
        self.left = left
        self.right = right 

class BST():
    ''' This Class contain 2 methods in order to convert given array to BST'''

    def sortedArrayToBST(self,nums):
        ''' This method responsible to sort the given array and return it as binary search tree'''
        nums.sort()
        def bst_tree(n):
            if not n:
                return None                                          
            m = len(n)//2
            return (TreeNode(n[m],bst_tree(n[:m]),bst_tree(n[m+1:])) )
        return bst_tree(nums)
def pre_order(root , x): 
    ''' This function take the root of the binary tree and sorted it as pre_order and append it into a empty list '''
    if root is not None:
        x.append(root.val)
    if root.left is not None:
        pre_order(root.left , x)
    if root.right is not None:
        pre_order(root.right , x)
    return x
        

if __name__ == "__main__":
    Array1 = BST()
    x=Array1.sortedArrayToBST([0,-3,-10,5,9])
    print(pre_order(x , []))

    Array2= BST()
    z = Array2.sortedArrayToBST([3,1])
    print(pre_order(z , []))

    
