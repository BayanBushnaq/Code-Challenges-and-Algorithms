# Write here the code challenge solution

class TreeNode():
    ''' This Main Class responsible to define any given array to Tree'''
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val 
        self.left = left
        self.right = right 

  

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



def findsum(root,k):
    ''' This function take the root of tree and reorder it and return it as BST then looping inside the tree 
    and testing if the summation of 2 nodes are in the tree or not'''
    bst = pre_order(root,[])
    for i in range(len(bst)):
        if (bst[i] - k ) not in bst:
            continue
        else:
            return True
    else:
        return False



if __name__=="__main__":
    tree1 = TreeNode()
    x=tree1.sortedArrayToBST([7,2,9,1,5,14])
    print(findsum(x,4))
    
    

    




