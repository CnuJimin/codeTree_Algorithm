n, m = map(int, input().split())

a_arr = [0] * 1000001
b_arr = [0] * 1000001

#a이동 
time = 0 
#n번 이동 
for i in range(n):
    v, t = map(int, input().split())

    #t시간동안 v만큼 이동함 
    for j in range(1, t+1):
        time += 1
        a_arr[time] = a_arr[time - 1] + v


#b이동 
time = 0 
#m번 이동 
for i in range(m):
    v, t = map(int, input().split())

    #t시간동안 v만큼 이동함 
    for j in range(1, t+1):
        time += 1
        b_arr[time] = b_arr[time - 1] + v


#선두 몇번 바뀌었는지 확인 

change_arr = [0] * (time + 1)

ans = 0 
for i in range(1, time + 1):
    if a_arr[i] - b_arr[i] >= 0 :
        change_arr[i] = 1
    else:
        change_arr[i] = -1


for i in range(1, len(change_arr) - 2):
    if change_arr[i] != change_arr[i + 1]:
        ans += 1

print(ans)
