from collections import deque 

dq = deque()

n = int(input())

for _ in range(n):
    arr = tuple(map(str, input().split()))

    if arr[0] == "push_front":
        dq.appendleft(arr[1])
    elif arr[0] == "push_back":
        dq.append(arr[1])
    elif arr[0] == "pop_front":
        print(dq.popleft())
    elif arr[0] == "pop_back":
        print(dq.pop())
    elif arr[0] == "size":
        print(len(dq))
    elif arr[0] == "empty":
        if dq:
            print("0")
        else:
            print("1")
    elif arr[0] == "front":
        print(dq[0])
    elif arr[0] == "back":
        print(dq[-1])
