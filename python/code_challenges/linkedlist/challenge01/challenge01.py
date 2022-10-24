# Write here the code challenge solution

from classLinkedList import LinkedListNode , Linkedlist



def deletegivenNode(node):
    if node.nextNode != None : 
        node.value = node.nextNode.value
        node.nextNode = node.nextNode.nextNode
            

if __name__ == '__main__':
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
    deletegivenNode(node2)
    # print(node2.value)
    print(ll.printLinkedList())











