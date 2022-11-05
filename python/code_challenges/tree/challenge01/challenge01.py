# Write here the code challenge solution

class TreeNode:
    '''Initial class that takes value for node , left and right node  '''
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val 
        self.left = left
        self.right = right

class BinaryTree:
    '''This class take preorder tree , in_order Tree and return the Binary Tree for the given both trees '''
    def buildtree(self , preorder , inorder):
        
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildtree(preorder, inorder[:INDEX])
            root.right = self.buildtree(preorder, inorder[INDEX+1:])
            return root

    

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
    tree1 = BinaryTree()
    x = tree1.buildtree([3,9,20,15,7],[9,3,15,20,7])
    print(pre_order(x , []))
   

    tree2 = BinaryTree()
    y = tree2.buildtree([-1],[-1])
    print(pre_order(y , []))
    
    

    
