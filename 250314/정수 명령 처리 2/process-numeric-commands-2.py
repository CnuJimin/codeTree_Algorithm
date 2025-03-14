from collections import deque

class Queue: 
    def __init__ (self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def pop(self):
        return self.dq.popleft()
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        if not self.dq:
            return "1"
        else:
            return "0"

    def front(self):
        return self.dq[0]


q = Queue()

n = int(input())

for _ in range(n):
    arr = tuple(map(str, input().split()))

    if arr[0] == "push":
        q.push(arr[1])
    elif arr[0] == "pop":
        print(q.pop())
    elif arr[0] == "size":
        print(q.size())
    elif arr[0] == "empty":
        print(q.empty())
    elif arr[0] == "front":
        print(q.front())