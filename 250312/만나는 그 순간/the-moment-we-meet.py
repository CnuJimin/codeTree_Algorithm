# A -> n번, B-> m 번 움직임 
# 배열의 크기는 1000 몇 초 동안 어디 위치인지를 기록함 

n, m = map(int, input().split())

A_arr = [0] * 1000001
B_arr = [0] * 1000001

def move (num, arr):
    #현재 시간 
    cur = 0
    #현재 위치 
    pos = 0 
    for _ in range(num):
        way, t = map(str, input().split())
        t = int(t)

        #만약 방향이 R이라면 t시간에 걸쳐 현재 위치에 +1 
        if way == "R":
            for i in range(t):
                cur += 1
                pos += 1
                arr[cur] = pos 
        
        else:
            for i in range(t):
                cur += 1
                pos -= 1
                arr[cur] = pos


    return arr 

A_arr = move(n, A_arr)
B_arr = move(m, B_arr)

for i in range(1, 1000001):
    if A_arr[i] == B_arr[i]:
        print(i)
        break



