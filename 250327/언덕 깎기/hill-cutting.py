#최저 높이와 최고 높이를 찾고
#정렬을 하고, 차례대로 맨 앞과 맨 뒤 를 한번씩 올리고 내리는 것을 반복하는건 어떤가??

n = int(input())

arr = [int(input()) for _ in range(n)]
low_cost = 0 
high_cost = 0 
while True:
    arr.sort()
    #가장 낮은 언덕과 가장 높은 언덕의 높이 차가 17이하면 멈춤 
    if arr[-1] - arr[0] <= 17:
        break
    
    arr[0] += 1 
    low_cost += 1
    if arr[-1] - arr[0] <= 17:
        break


    arr[-1] -= 1
    high_cost += 1
    if arr[-1] - arr[0] <= 17:
        break

print(low_cost * low_cost + high_cost *high_cost)