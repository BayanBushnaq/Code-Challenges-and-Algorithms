

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