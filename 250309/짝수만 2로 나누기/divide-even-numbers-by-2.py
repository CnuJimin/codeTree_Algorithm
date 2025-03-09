n = int(input())

arr = list(map(int, input().split()))

def even(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2

even(arr)

print(*arr)