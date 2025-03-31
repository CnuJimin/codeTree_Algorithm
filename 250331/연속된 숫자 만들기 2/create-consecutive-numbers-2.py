# 위치가 3개 주어지면, 가운데 기준으로 양 옆 중 가운데를 선택 함 

#연속된 세 수가 주어지면 -> 0
#세 수 중에 차이가 2나는 수가 있다면 -> 1 
# 다른 경우는 2 

arr = list(map(int, input().split()))

arr.sort()

if arr[2] - arr[1] == 1 and arr[1] - arr[0] == 1 :
    print(0)
elif arr[2] - arr[1] == 2 or arr[1] - arr[0] == 2 :
    print(1)
else:
    print(2)

