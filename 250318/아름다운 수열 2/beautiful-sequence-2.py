n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0 
for i in range(len(A) - len(B) + 1):
    if sorted(A[i:i+len(B)]) == sorted(B):
        ans += 1

print(ans)