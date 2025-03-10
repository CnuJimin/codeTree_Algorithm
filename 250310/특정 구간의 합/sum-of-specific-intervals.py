n, m = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(m):
    a,b = tuple(map(int, input().split()))
    a, b = a-1,b-1
    
    total = 0
    for j in range(a, b+1):
        total += arr[j]
    
    print(total)
    