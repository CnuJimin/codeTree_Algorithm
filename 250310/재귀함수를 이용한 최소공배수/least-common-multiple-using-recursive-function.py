n = int(input())

arr = list(map(int, input().split()))

n = n - 1




def maxCommon(a,b):

    max_value = max(a, b)
    min_value = min(a, b)

    for i in range(1, min_value + 1):
        if i * max_value % min_value == 0:
            return i * max_value

def func(n):
    if n == 0 : 
        return arr[0]
    
    return maxCommon(func(n-1), arr[n])


print(func(n))
    

