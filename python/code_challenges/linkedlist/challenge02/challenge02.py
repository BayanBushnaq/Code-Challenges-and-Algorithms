# Write here the code challenge solution




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

    def middleNode(self):
        mid = self.head
        count = 0

        while self.head:
 
            
            if (count & 1):
                mid = mid.nextNode
            self.head = self.head.nextNode
 
            
            count += 1
        print(mid.value)
        # while temp != None:
        #     print(temp.value)
        #     temp=temp.nextNode
            

if __name__ == "__main__":
    ll=Linkedlist()
    print(ll.printLinkedList())

    node1=LinkedListNode(2)
    ll.insert(node1)
    print(ll.printLinkedList())

    node2 = LinkedListNode(55)
    ll.insert(node2)
    print(ll.printLinkedList())
    

    node3 = LinkedListNode(44)
    ll.insert(node3)
    print(ll.printLinkedList())
    ll.middleNode()
    print(ll.printLinkedList())

    node4 = LinkedListNode(66)
    ll.insert(node4)
    ll.middleNode()
    print(ll.printLinkedList())


