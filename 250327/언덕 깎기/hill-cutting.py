import sys
#최저 높이와 최고 높이를 찾고
#정렬을 하고, 차례대로 맨 앞과 맨 뒤 를 한번씩 올리고 내리는 것을 반복하는건 어떤가??

n = int(input())
k = 17

arr = [int(input()) for _ in range(n)]

ans = sys.maxsize


for i in range(101):
    cost = 0 

    for j in range(n):

        if arr[j] > i + k:
            cost += (arr[j] - i - k) * (arr[j] - i - k)
        
        elif arr[j] < i :
            cost += (i - arr[j]) * (i - arr[j])
        
    
    ans = min(ans, cost)

print(ans)