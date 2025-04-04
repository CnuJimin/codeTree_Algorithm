arr = list(map(int, input().split()))

arr.sort()

a = arr[0] 
b = arr[1]
if arr[2] == a+b:
    c = arr[3]
else:
    c = arr[2]

print(a,b,c)