# Write here the code challenge solution

class Queue(object):
    ''' this class contain 3 4 methods which is resbonsible to implement queue in 2 stacks'''
    def __init__ (self):
        self.stack1=[]
        self.stack2=[]

    def push(self,item):
        '''this method enqueue the item into stack1'''
        for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        self.stack1.append(item)

        

    def pop(self):
        ''' this method resbonsible to dequeue the items from stack1 and dequeue it into stack2'''
        if len(self.stack2) == 0:
            return "The Queue is empty"
        else : 
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        ''' this method resbonsible to get the top of the stack2'''
        # if len(self.stack1) == 0:
        #     return "The Queue is empty"
        #
        # else : 
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        # for i in range(len(self.stack2)):
            # if i == (len(self.stack2)-1):
                # return self.stack2[i]
       

    def empty(self):
        ''' this method resbonsible to check if the stack2 is empty or not'''
        #return len(self.stack2)
        if len(self.stack2) >= 1:
            return "The Queue is not empty :)"
        else:
            return "the Queue is empty !"

if __name__=="__main__":
    MyQueue = Queue()
    MyQueue.push(1) #queue is: [1]
    MyQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
    
    print(MyQueue.peek()) # return 1
    print(MyQueue.pop()) # return 1, queue is [2]
    print(MyQueue.empty())
    MyQueue.push(3)
    print(MyQueue.peek())
    print(MyQueue.pop())
    print(MyQueue.peek())


