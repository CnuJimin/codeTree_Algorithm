x1,x2,x3,x4 = map(int, input().split())

arr = [0] * 110

for i in range(x1,x2+1):
    arr[i] += 1

for i in range(x3,x4+1):
    arr[i] += 1

flag = False

for i in arr:
    if i > 1:
        flag = True

if flag:
    print("intersecting")
else:
    print("nonintersecting")

