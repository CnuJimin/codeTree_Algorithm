n = int(input())

ranges = [tuple(map(int,input().split())) for _ in range(n)]

arr = [0] * 101

for x1,x2 in ranges:
    for i in range(x1,x2+1):
        arr[i] += 1


flag = False

for i in arr:
    if i == n :
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")