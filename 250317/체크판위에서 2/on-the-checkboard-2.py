#배열을 돌면서 , B를 찾고, 해당 B와 마지막 행,열의 차이만큼 곱하기 

r,c = map(int, input().split())

arr = [list(map(str, input().split()))for i in range(c)]

cnt = 0 

for x in range(1, r - 1):
    for y in range(1, c - 1):
        if arr[x][y] == "B":
            cnt += (r - x - 2) * (c - y - 2)
    
print(cnt)