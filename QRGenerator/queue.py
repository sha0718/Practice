from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
         self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

pq = Queue()
pq.enqueue({
 'company' : "amazon",
 'prices' : 134

})

pq.enqueue({
 'company' : "amazon",
 'prices' : 128
 
})    

pq.enqueue({
 'company' : "amazon",
 'prices' : 132
 
})
if __name__ == '__main__':
  print(pq.buffer)
  print(pq.dequeue())
  print(pq.size())
    
