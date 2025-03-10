n ,m = map(int, input().split())

arr = list(map(int, input().split()))

def makeSum(m, arr):
    sum = 0 
    while True:
        # print(m)
        sum += arr[m - 1]
        if m == 1 :
            break
        if m % 2 == 0 :
            m //= 2 
        else:
            m -= 1
    
    return sum 

print(makeSum(m, arr))
        