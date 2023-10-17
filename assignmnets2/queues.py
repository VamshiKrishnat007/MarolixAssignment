from collections import deque



class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def size(self):
        return len(self.buffer)
    
pq=Queue()
pq.enqueue({"comany":"wall Mart", "timestamp":"15 apr, 11:01 AM", "price":150})
pq.enqueue({"comany":"wall Mart", "timestamp":"16 apr, 11:02 AM", "price":250})
print(pq.buffer)
print(pq.size() )
print(pq.dequeue())
print(pq.buffer)
       