import sys
t, a, b = map(int, input().split())

arr = [0] * 1001

for _ in range(t):
    alp, pos = input().split()
    pos = int(pos)
    arr[pos] = alp

ans = 0 

#k의 위치를 정함
for k in range(a, b+1):
    d1 = sys.maxsize
    d2 = sys.maxsize

    #k의 위치를 기준으로 S,N을 찾음 
    for j in range(1, 1001):
        if arr[j] == "S":
            #k와의 거리가 가장 가까운 S를 찾기 
            # print("S위치 = ", j)
            dist_1 = abs(k - j)
            d1 = min(dist_1, d1)
        
        if arr[j] == "N":
            # print("N위치 = ", j)
            dist_2 = abs(k - j)
            d2 = min(dist_2,d2)
        
    if d1 <= d2:
        # print(f"k위치 = {k}")
        # print(d1,d2)
        ans += 1

print(ans)