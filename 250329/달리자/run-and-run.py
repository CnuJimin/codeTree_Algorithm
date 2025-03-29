#뒤에서부터 이동해서 채우면 최소가 될 것 같음 
n = int(input())

before = list(map(int, input().split()))
after = list(map(int, input().split()))

ans = 0
for i in range(n):
    if before[i] > after[i]:
        num = before[i] - after[i]

        before[i] -= num
        before[i+1] += num
        ans += num 

print(ans)