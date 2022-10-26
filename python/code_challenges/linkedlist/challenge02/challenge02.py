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
        ''' this method responsible to print the whole linkedlist  '''
        x=""
        currentNode= self.head
        while currentNode is not None:
            x+= f'{currentNode.value} => ' 
            currentNode=currentNode.nextNode
        x+='None'
        return x

    def middleNode(self):
        ''' this methos responsible to find the middle node in the linked list and return the whole 
        linked list after the middle '''
        slow = self.head
        fast = self.head
        x = []
        current = self.head
        while current is not None:
            x.append(current.value)
            current = current.nextNode

        if self.head is not None:
            while (fast is not None and fast.nextNode is not None):
                fast = fast.nextNode.nextNode
                slow = slow.nextNode
            #print("The middle element is: ", slow.value)
            y = int(len(x)/2)
            z = len(x)
            w=[]
            #print("The rest of LinkedList after middle =>")
            for i in range(y,z):
                w.append(x[i])
            return w
                #print(x[i])
                
                        

if __name__ == "__main__":
    ll=Linkedlist()
    #print(ll.printLinkedList())

    node1=LinkedListNode(2)
    ll.insert(node1)
    #print(ll.printLinkedList())

    node2 = LinkedListNode(55)
    ll.insert(node2)
    #print(ll.printLinkedList())
    

    node3 = LinkedListNode(44)
    ll.insert(node3)
    #print(ll.printLinkedList())
    #ll.middleNode()
    #print(ll.printLinkedList())

    node4 = LinkedListNode(66)
    ll.insert(node4)
    print(ll.printLinkedList())
    print(ll.middleNode())
    #print(ll.printLinkedList())




    llist=Linkedlist()

    node1=LinkedListNode(1)
    llist.insert(node1)

    node2 = LinkedListNode(2)
    llist.insert(node2)

    node3 = LinkedListNode(4)
    llist.insert(node3)

    node4 = LinkedListNode(6)
    llist.insert(node4)

    node5 = LinkedListNode(11)
    llist.insert(node5)


    print(llist.printLinkedList())
    print(llist.middleNode())
    

    
    


