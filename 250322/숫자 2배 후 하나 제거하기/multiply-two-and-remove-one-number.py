import sys
n = int(input())
nums = list(map(int, input().split()))
backup = nums[:]

ans = sys.maxsize
#n개의 수중 하나를 선택해서 2배 해준다
for i in range(n):
    nums[i] *= 2 
    #n개의 수 중 하나를 뺀 배열을 만들고, 인접한 숫자간의 합을 구한 뒤 최솟값을 갱신한다. 
    for j in range(n):
        diff = 0 
        remain = [] 
        for k, elment in enumerate(nums):
            if k == j :
                continue 
            
            remain.append(elment)
        
        for k in range(n-2):
            diff += abs(remain[k] - remain[k+1])
        
        ans = min(diff, ans)
    
    nums = backup[:]

print(ans)