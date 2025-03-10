n = int(input())

arr = list(map(int, input().split()))

arr.sort()
#2 3 5 5
#1 2 3 5 7 8
max_value = 0

for i in range(n):
    max_value = max(max_value, arr[i] + arr[2*n-1-i])

print(max_value)