import sys
n = int(input())

arr = list(map(int, input().split()))
arr.sort()

# 2 5 7 9 10 15
#1~n-1 까지 +n 과 쌍을 이루게 하면 됨 

pair = []

for i in range(n):
    pair.append((arr[i], arr[i + n]))
# print(*pair)

ans = sys.maxsize

for i in range(n):
    a, b = pair[i]
    ans = min(ans, abs(a-b))

print(ans)