# Write here the code challenge solution

class Node:
    """ Class Responsible to create a node """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """ Class Responsible to create a binary search tree """
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right




def has_sum(tree, target):
    ''' functuin responsible to check if summation of 2 nodes in BST are equal given target. '''
    # Create a stack to store the nodes we need to visit
    stack = []
    # Create a set to store the values of the nodes we have already visited
    visited = set()

    # Push the root node onto the stack and mark it as visited
    node = tree.root
    stack.append(node)
    # visited.add(node.value)

    # While there are nodes in the stack, visit the next one
    while stack:
        # Pop the next node from the stack
        node = stack.pop()
            # visited.add(node.right.value)
        # Check if the node's value plus the value of any visited nodes equals the target
        for visited_val in visited:
            if (node.value + visited_val) == target:
                return True
        visited.add(node.value)
        # Push the node's children onto the stack and mark them as visited
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # If we've visited all the nodes and no pair sums to the target, return False
    return False

if __name__=="__main__":
    tree = BinarySearchTree()
    tree.insert(7)
    tree.insert(2)
    tree.insert(9)
    tree.insert(1)
    tree.insert(5)
    tree.insert(14)
    

# Test the has_sum function
    print(has_sum(tree, 3)) 
    print(has_sum(tree, 4))   
    print(has_sum(tree,9))
    print(has_sum(tree,15))
    
    

    
    

    




