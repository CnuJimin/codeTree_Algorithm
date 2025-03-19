#선분이 겹치게 되는 기준 -> x2가 그 전 수의 x2보다 앞에 있을 때 겹침
# 선분을 정렬하고, 자기보다 앞에 있는 선분들의 x2 값의 최댓값 기준으로 그것보다 앞에 있으면 겹치는 선분 

n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

lines.sort(key = lambda x : x[0])

max_y = lines[0][1]

# print(*lines)

ans = 1 
for i in range(1, n):
    x,y = lines[i]

    if y <= max_y:
        ans += 1
        # print("max_y = ", max_y)
        # print("x2 = ", y)



    if y > max_y:
        max_y = y 
    



print(n - ans)