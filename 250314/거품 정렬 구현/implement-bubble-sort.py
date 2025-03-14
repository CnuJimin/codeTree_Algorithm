n = int(input())
arr = list(map(int, input().split()))


while True : 
    flag = True

    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            flag = False
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp 
    # print(*arr)

    if flag :
        break


print(*arr)