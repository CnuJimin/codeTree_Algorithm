from collections import deque

n, k = map(int, input().split())

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def pop(self):
        return self.dq.popleft()
    
    def size(self):
        return len(self.dq)

    def front(self):
        return self.dq[0]
    

q = Queue()

for i in range(1, n+1):
    q.push(i)

# for i in range(q.size()):
#     print(q.dq[i], end = " ")

while q.size() != 1:

    for _ in range(k-1):
        q.push(q.front())
        q.pop()
    
    print(q.pop(), end = " ")

print(q.pop())