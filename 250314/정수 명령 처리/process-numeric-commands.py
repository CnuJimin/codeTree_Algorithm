class Stack: 
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0 :
            return "1"
        else:
            return "0"
    
    def top(self):
        return self.items[len(self.items) - 1]

s = Stack()

n = int(input())

for i in range(n):
    do = tuple(map(str, input().split()))

    if do[0] == "push":
        s.push(do[1])
    elif do[0] == "pop":
        print(s.pop())
    elif do[0] == "size":
        print(s.size())
    elif do[0] == "empty":
        print(s.empty())
    elif do[0] == "top":
        print(s.top())
