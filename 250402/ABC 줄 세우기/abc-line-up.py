#자기 자리에 맞지 않는 수의 개수를 구해서 해당 개수의 -1이 정답 

#0이면 그냥 0임 

n = int(input())

arr = list(input().split())

for i in range(n):
    char = arr[i]
    arr[i] = ord(char) - 65 

#앞에서부터 자기 자리 찾아서 이동 

cnt = 0

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            cnt += 1 


     
print(cnt)