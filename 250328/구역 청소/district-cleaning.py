#b와 c의 크기를 비교함, b<=c 이면 b-a + d-c / c<b이면 d-a

a,b = map(int, input().split())
c,d = map(int, input().split())

arr = [0] * 110

for i in range(a,b):
    arr[i] += 1

for i in range(c, d):
    arr[i] += 1

ans = 0 
for i in arr:
    if i >= 1 :
        ans += 1

print(ans)