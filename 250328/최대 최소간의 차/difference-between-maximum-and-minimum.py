import sys
n, k = map(int, input().split())

arr = list(map(int, input().split()))

#최솟값을 정하고, 모든 수가 [최솟값, 최솟값 + k] 안에 있도록 한 뒤, 비용을 구하고, 최솟값을 갱신함 


ans = sys.maxsize

# print(*arr)
#최솟값 설정
for i in range(1, 10001):
    cost = 0 
    # print("최솟값: ",i)
    for j in range(n):
        if arr[j] < i :
            cost += abs(i - arr[j])
        elif arr[j] > i + k :
            cost += abs(arr[j] - i - k)
        # print(cost)
    
    ans = min(ans, cost)

print(ans)