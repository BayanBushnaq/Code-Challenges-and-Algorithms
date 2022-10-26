# Write here the code challenge solution

class LinkedListNode:
    ''' this class is resposible to create a Node which is take 1 param , value 
    and selecet a pointer for the node to none as a default value or to the next node '''
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode


class Linkedlist:
    ''' this class is responsible to create a lonked list and connect it with each other '''
    def __init__(self):
        self.head = None

    def insert(self,node):
        ''' this method responsible to insert any node to the linked list '''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.nextNode is not None:
                current = current.nextNode
            current.nextNode = node

    def printLinkedList(self):
        ''' this method responsible to print the whole linkedlist '''
        x=""
        currentNode= self.head
        while currentNode is not None:
            x+= f'{currentNode.value} => ' 
            currentNode=currentNode.nextNode
        x+='None'
        return x
 
    def remove_nth_node(self,number):
        ''' This method responsible remove the nth node from the end of the list and return its head'''

        fast = slow = self.head
        for i in range (number):
            
            fast=fast.nextNode

        if fast is None:
            self.head=self.head.nextNode
            return self.head

        while fast.nextNode:
            fast = fast.nextNode
            slow = slow.nextNode
        slow.nextNode = slow.nextNode.nextNode
        return self.head 
        
 
        
if __name__ == "__main__":
    ll=Linkedlist()
    

    node1=LinkedListNode(2)
    ll.insert(node1)
   

    node2 = LinkedListNode(55)
    ll.insert(node2)
    
    
    node3 = LinkedListNode(44)
    ll.insert(node3)
   

    node4 = LinkedListNode(66)
    ll.insert(node4)
    print(ll.printLinkedList())
    ll.remove_nth_node(4)
    print(ll.printLinkedList())    
        
        

