n = int(input())
arr = list(map(int, input().split()))


for i in range(n-1):
    min_value = i
    for j in range(i+1, n):
        if arr[j] < arr[min_value]:
            min_value = j
        
    temp = arr[i]
    arr[i] = arr[min_value]
    arr[min_value] = temp 

print(* arr)
