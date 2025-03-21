#1~3번에 조약돌이 있다고 생각하고 

#N번 반복하면서 a,b의 위치를 바꾸고, c위치의 배열을 확인해서, 값이 있으면 + 1 
n = int(input())
ans = 0 

pattern = [tuple(map(int, input().split())) for _ in range(n)]

for rock in range(1,4):
    arr = [0] * 4
    arr[rock] = 1 
    cnt = 0 
    for i in range(n):
        a,b,c = pattern[i]
        temp = arr[b]
        arr[b] = arr[a]
        arr[a] = temp

        if arr[c] == 1 :
            cnt += 1 
    
    ans = max(ans, cnt)

print(ans)