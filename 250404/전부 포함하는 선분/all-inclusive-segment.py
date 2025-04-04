import sys
n = int(input())

x1 = []
x2 = []

for i in range(n):
    a,b = tuple(map(int, input().split()))
    x1.append(a)
    x2.append(b)

ans = sys.maxsize
for i in range(n):
    ans = min(ans, max(x2[:i] + x2[i+1:]) - min(x1[:i] + x1[i+1:]))

print(ans)