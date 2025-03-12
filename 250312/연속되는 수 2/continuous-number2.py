n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
answer = -1
for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
        answer = max(cnt, answer)
    
    else:
        cnt = 1
        answer = max(cnt, answer)

print(answer)