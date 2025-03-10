n = int(input())
arr = list(map(int, input().split()))

n = n-1

def getMax(n):
    if n == 0 :
        return arr[0]

    return max(arr[n], getMax(n-1))

print(getMax(n))
