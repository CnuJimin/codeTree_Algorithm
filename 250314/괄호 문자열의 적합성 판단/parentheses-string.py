class Stack():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def empty(self):
        if len(self.items) == 0 :
            return True
        else:
            return False

s = Stack()

arr = list(input())

n = len(arr)

ans = ""

for i in range(n):
    if arr[i] == "(":
        s.push(arr[i])

    else:
        if s.empty():
            ans = "No"
        else:
            s.pop()

    # print(*s.items)
    

if not s.empty():
    ans = "No"
else:
    ans = "Yes"

print(ans)
        