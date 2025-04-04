#블럭들 개수 더하고 나누기 n 해서, 최소 블럭 개수를 구함
#블럭들 중에서 최소 블럭 개수보다 큰 값들에서 최소 블럭 개수를 뺀 값을 다 더함 

n = int(input())

arr = [int(input()) for _ in range(n)]

avr = sum(arr) // n
ans = 0 


for i in arr:
    if i > avr:
        ans += i - avr

print(ans)