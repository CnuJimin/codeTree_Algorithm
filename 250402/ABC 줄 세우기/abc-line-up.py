#자기 자리에 맞지 않는 수의 개수를 구해서 해당 개수의 -1이 정답 

#0이면 그냥 0임 

n = int(input())

arr = list(input().split())

for i in range(n):
    char = arr[i]
    arr[i] = ord(char) - 65 

cnt = 0 

for i in range(n):
    if i != arr[i]:
        cnt += 1

if cnt == 0 :
    print(0)
else:
    print(cnt - 1)