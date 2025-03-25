import sys

n, k = map(int, input().split())

arr = list(map(int, input().split()))

#최댓값 설정해야 함, 그런데 처음과 마지막 지점은 항상 가야하기 때문에, 최솟값이 이 둘을 넘을 순 없음 
#최댓값이 최소가 되도록 한다.. 

ans = sys.maxsize

def possible(num):
    index = [] 
    for i in range(n):
        if arr[i] <= num :
            index.append(i)
    
    for i in range(len(index)-1):
        if abs(index[i] - index[i+1]) > k :
            return False
    
    return True 

for i in range(max(arr), max(arr[0], arr[-1]) - 1, -1):
    # print(i)
    if possible(i):
        ans = min(ans, i)

print(ans)


