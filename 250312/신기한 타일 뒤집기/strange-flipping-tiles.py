# 총 배열의 길이 200_010 

arr = [0] * 200010

n = int(input())

# 시작위치 100005에서 명령을 받음 
x = 100005
# n번의 명령에 대해서 
for i in range(n):
    dist, way = map(str, input().split())
    dist = int(dist)
    # 현재 위치부터 시작해 n개의 칸을 색칠 [검정 = 1, 흰색 = 2]
    if way == "R":
        arr[x] = 1
        for _ in range(dist - 1): 
            x += 1
            arr[x] = 1

            # print(x)
    else: 
        arr[x] = 2
        for _ in range(dist - 1): 
            x -= 1
            arr[x] = 2

            # print(x)

# 색을 다칠하고 배열을 돌면서 검정과 흰색의 개수를 구함 
white, black = 0, 0
for i in arr:
    if i == 1 :
        black += 1
    elif i == 2:
        white += 1

print(white, black)