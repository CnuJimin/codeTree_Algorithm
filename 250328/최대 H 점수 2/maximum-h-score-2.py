#모든 경우에 대해 -> 최댓값을 설정함, 최댓값 보다 1보다 작은 수는 1을 더할 수 있음, L보다 
#할거 한다 

n, l = map(int, input().split())

arr = list(map(int, input().split()))

def satisfy_h(array, m):
    cnt = 0 

    for i in range(n):
        if array[i] >= m :
            cnt += 1
    
    if cnt >= m :
        return True
    else:
        return False


ans = 0 
#최댓값 설정 
for i in range(1, 101):
    up = l 
    nums = arr[:]
    #최댓값 i에 대해 H를 만족하는지 검사 
    for j in range(n):
        if nums[j] == i - 1 and up > 0:
            nums[j] += 1 
            up -= 1
        
        if satisfy_h(nums, i):
            ans = max(ans, i)

print(ans)



