# offset을 고려해서 배열의 크기를 [2050][2050]으로 설정함 
arr = [[0 for i in range(2051)] for i in range(2051)]

x1,y1,x2,y2 = map(int, input().split())
x1,y1,x2,y2 = x1 + 1025, y1 + 1025, x2 + 1025, y2 + 1025
# x, y = 1025, 1025 

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 1


x1,y1,x2,y2 = map(int, input().split())
x1,y1,x2,y2 = x1 + 1025, y1 + 1025, x2 + 1025, y2 + 1025

# x, y = 1025, 1025 

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 0 


max_x, min_x, max_y, min_y = 0, 3000, 0, 3000

exist_sqaure = True

for i in range(2051):
    for j in range(2051):
        if arr[i][j] == 1 :
            exist_sqaure = True
            min_x = min(i, min_x)
            min_y = min(j, min_y)
            max_x = max(i, max_x)
            max_y = max(j, max_y)


if exist_sqaure :
    print((max_x - min_x + 1) * (max_y - min_y + 1))
else:
    print("0")