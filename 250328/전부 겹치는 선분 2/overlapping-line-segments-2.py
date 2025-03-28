n = int(input())

ranges = [tuple(map(int, input().split())) for _ in range(n)]

flag = False

for i in range(n):
    arr = [0] * 110

    for j in range(n):
        if i == j :
            continue
        
        x1,x2 = ranges[j]

        for k in range(x1,x2+1):
            arr[k] += 1
    
    for j in arr:
        if j == n-1 :
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")