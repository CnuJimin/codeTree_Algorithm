n, m = map(int, input().split())

a_arr = [0] * 2000010
b_arr = [0] * 2000010

#A의 이동 
a_time = 0

for _ in range(n):
    dist, way = map(str, input().split())
    dist = int(dist)

    if way == "L":
        for i in range(dist):
            a_time += 1
            a_arr[a_time] = a_arr[a_time - 1] - 1
    else:
        for i in range(dist):
            a_time += 1
            a_arr[a_time] = a_arr[a_time - 1] + 1
    
    # print(a_arr[time])


#B의 이동 
b_time = 0 

for _ in range(m):
    dist, way = map(str, input().split())
    dist = int(dist)

    if way == "L":
        for i in range(dist):
            b_time += 1

            b_arr[b_time] = b_arr[b_time - 1] - 1
    else:
        for i in range(dist):
            b_time += 1

            b_arr[b_time] = b_arr[b_time - 1] + 1
    # print(b_arr[time])

if a_time < b_time:
    for i in range(a_time + 1, b_time + 1):
        if a_arr[i] == 0:
            a_arr[i] = a_arr[a_time]
else:
    for i in range(b_time + 1, a_time + 1):
        if b_arr[i] == 0:
            b_arr[i] = b_arr[b_time]




max_time = max(a_time, b_time)






answer = 0 


# for i in range(1, time + 1):
#     print(a_arr[i], end = " ")

# print()
# for i in range(time + 1):
#     print(b_arr[i], end = " ")




for i in range(1, max_time):
    if a_arr[i] != b_arr[i] and a_arr[i+1] == b_arr[i+1]:
        # print(i)
        answer += 1 

print(answer)