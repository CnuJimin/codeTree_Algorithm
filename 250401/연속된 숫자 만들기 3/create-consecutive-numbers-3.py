#바로 옆으로 이동하면 됨 
arr = list(map(int ,input().split()))
arr.sort

#처음부터 1열로 서 있을 때 -> 0
if arr[1] - arr[0] == 1 and arr[2] - arr[1] == 1:
    print(0) 
#둘 중 하나가 2차이 날 때 -> 1
elif arr[1] - arr[0] == 2 or arr[2] - arr[1] == 2 :
    print(1)
else:
    print(max(arr[1] - arr[0], arr[2] - arr[1]) - 1)
#12 7 -> 267 -> 236 -> 346 -> 456 3456 아닌 경우는 차이 중 큰 수의 n - 1