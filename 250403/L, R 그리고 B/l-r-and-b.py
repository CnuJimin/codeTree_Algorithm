#그냥 L에서 B의 좌표값을 빼면됨 

arr = [list(input()) for _ in range(10)]

x1,y1 = 0,0
x2,y2 = 0,0
x3,y3 = 0,0
for i in range(10):
    for j in range(10):
        if arr[i][j] == "B":
            x1,y1 = i,j
        if arr[i][j] == "L":
            x2,y2 = i,j
        if arr[i][j] == "R":
            x3,y3 = i,j

# print(x1,y1)
# print(x2,y2)

if x3 == x1 == x2:
    if y1<y3<y2 or y1>y3>y2:
        print(1 + abs(y2-y1))
    if max(y1,y2)<y3 or min(y1,y2)>y3:
        print(abs(y2-y1)-1)
elif y1== y2 == y3:
    if x1<x3<x2 or x1>x3>x2:
        print(1 + abs(x2-x1))
    if max(x1,x2)<x3 or min(x1,x2)>x3:
        print(abs(x2-x1)-1)
else:
    print(abs(x2-x1) + abs(y2-y1) - 1)
