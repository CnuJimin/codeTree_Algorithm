n, m = map(int, input().split())

#a배열
a_arr = [0] * 2000010
#b배열
b_arr = [0] * 2000010
#선두 기록 배열 
fastOne = [0] * 2000010

#a 이동 기록 
time = 0 
for _ in range(n):
    v, t = map(int, input().split())

    #t초동안 이동 
    for i in range(t):
        time += 1
        a_arr[time] = a_arr[time - 1] + v


#b 이동 기록 
time = 0 
for _ in range(m):
    v, t = map(int, input().split())

    #t초동안 이동 
    for i in range(t):
        time += 1
        b_arr[time] = b_arr[time - 1] + v


for i in range(1, time + 1):
    if a_arr[i] > b_arr[i]:
        fastOne[i] += 1
    elif a_arr[i] < b_arr[i]:
        fastOne[i] += 2
    elif a_arr[i] == b_arr[i]:
        fastOne[i] += 3


ans = 1 

for i in range(1, time):
    # print(fastOne[i], end = " ")
    if fastOne[i] != fastOne[i + 1]:
        ans += 1





print(ans)



#1 2 6 7 9 11 13 15 17 19 21 23 25 27 
#2 4 6 7 8 11 14 17 20 23 26 29 32 35