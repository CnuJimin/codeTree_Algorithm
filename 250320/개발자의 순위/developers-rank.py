k, n = map(int, input().split())

race = [list(map(int, input().split())) for _ in range(k)]

ans = 0
#i번 선수가 
for i in range(1, n+1):
    for j in range(1, n+1):
        flag = True
        if i == j :
            continue
        for t in range(k):
            for l in range(n):
                for o in range(n):
                    if race[t][l] == i and race[t][o] == j :
                        if l > o :
                            flag = False
        
        if flag:
            # print(i,j)
            ans += 1
print(ans)
#j번 선수보다 앞서 있었는지 확인
#한번이라도 뒤쳐지면 false 