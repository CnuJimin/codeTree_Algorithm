import sys
N = int(input())
arr = list(map(int, input().split()))

min_value = sys.maxsize

# 모든 경우에 대해 모든 i에 대해 
for i in range(N):
    dist = 0

# 할 거 한다 i와 j의 차이를 구함, 그런데 사람이 arr[j]만큼 살고 있으니까 이를 곱해줌 
    for j in range(N):
        dist += abs(i - j) * arr[j]
    min_value = min(min_value, dist)

print(min_value)

