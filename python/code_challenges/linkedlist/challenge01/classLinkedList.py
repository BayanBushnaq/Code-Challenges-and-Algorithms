

class LinkedListNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.nextNode is not None:
                current = current.nextNode
            current.nextNode = node

    def printLinkedList(self):
        x=""
        currentNode= self.head
        while currentNode is not None:
            x+= f'{currentNode.value} => ' 
            currentNode=currentNode.nextNode
        x+='None'
        return x