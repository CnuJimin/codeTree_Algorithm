n = int(input())

arr = list(map(int, input().split()))

def absolute(arr):
    for i in range(n):
        arr[i] = abs(arr[i])

absolute(arr)

print(*arr)