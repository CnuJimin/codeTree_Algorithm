n = int(input())

arr = [int(input()) for _ in range(n)]

cnt = 0 
answer = -1 

for i in range(n):
    if i == 0 or arr[i] * arr[i-1] > 0 :
        cnt += 1
        answer = max(answer, cnt)
    else:
        cnt = 1

print(answer)