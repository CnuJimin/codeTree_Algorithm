#1243 -> 4,3 사이에 넣어야 함 

#126354 -> 오름차순이 아닌 부분을 찾음 뒤에서부터 찾음 , 하나라도 찾으면 그 앞에수만큼 그냥 
#635124 -> 351246 -> 512346 -> 123456 -> 5

#124356 -> 오름차순이 아닌 부분을 찾음 
#435126 -> 351246 -> 512346 -> 123456 -> 5

n = int(input())
arr = list(map(int, input().split()))

flag = False
ans = 0 

for i in range(n-1, 0, -1):
    if arr[i] < arr[i-1]:
        ans = i 
        flag = True
        break

if flag:
    print(ans)
else:
    print(0)