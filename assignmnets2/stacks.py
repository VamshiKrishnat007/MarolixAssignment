class Stack(object):
    def __init__(self):
        self.stack=[]
        self.numOfItems=0
    def isEmpty(self):
        return self.stack==[]
    def push(self,data):
        self.stack.insert(self.numOfItems, data)
        self.numOfItems+=1
        return "{} pushed to stack".format(data)
    def pop(self):
        self.numOfItems-=1
        D=self.stack.pop(self.numOfItems)
        
        return "{} pop from stack".format(D)
    
    def retrive_stack_elements(self):
        return (self.stack)
    def size(self):
        return len(self.stack)

if __name__=="__main__":
    
    stacks=Stack()
    print(stacks.push(7))
    print(stacks.push(10))
    print(stacks.push(6))
    print(stacks.pop())
    print(stacks.pop())
    print(stacks.size())
    print(stacks.retrive_stack_elements())
    
    
        
    
    


# class Stack(object):
    
#     def __init__(self):
#         self.stack=[]
#         self.numOfItmes=0
#     def isEmpty(self):
#         return self.stack==[]
#     def  push(self, data):
#         self.stack.insert(self.numOfItmes,data)
#         self.numOfItmes+=1
#         return "{} pushed to stack".format(data)
#     def pop(self):
#         self.numOfItmes-=1
#         data=self.stack.pop(self.numOfItmes)
#         return "{} pop from stack".format(data)
#     def stackSize(self):
#         return (self.stack)

# # a=10
# # b=122

# if __name__=="__main__":
#     s=Stack()
   
#     print(s.push(2))
#     print(s.push(5))
#     print(s.push(20))
#     print(s.pop())
#     print(s.stackSize())
        
        
        
    