n, m = map(int, input().split())

a_arr = [0] * 2000010
b_arr = [0] * 2000010

#A의 이동 
time = 0

for _ in range(n):
    dist, way = map(str, input().split())
    dist = int(dist)

    if way == "L":
        for i in range(dist):
            time += 1
            a_arr[time] = a_arr[time - 1] - 1
    else:
        for i in range(dist):
            time += 1
            a_arr[time] = a_arr[time - 1] + 1
    
    # print(a_arr[time])


#B의 이동 
time = 0 

for _ in range(m):
    dist, way = map(str, input().split())
    dist = int(dist)

    if way == "L":
        for i in range(dist):
            time += 1

            b_arr[time] = b_arr[time - 1] - 1
    else:
        for i in range(dist):
            time += 1

            b_arr[time] = b_arr[time - 1] + 1
    # print(b_arr[time])


answer = 0 


for i in range(1, time + 1):
    if a_arr[i] != b_arr[i] and a_arr[i+1] == b_arr[i+1]:
        answer += 1 

print(answer)