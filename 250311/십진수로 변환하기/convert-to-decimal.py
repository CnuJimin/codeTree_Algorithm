arr = list(input())
arr = list(map(int, arr))

num = 0 

for i in range(len(arr)):
    num = num * 2  + arr[i]

print(num)