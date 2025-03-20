n, m, d, s = map(int, input().split())

arr = [[0 for _ in range(51)]for _ in range(51)]

eat = [list(map(int, input().split())) for _ in range(d)] # [몇번쨰 사람, 몇번째 치즈, 시간]

sick = [list(map(int, input().split())) for _ in range(s)] # [몇번째 사람, 언제아팠는지]

spoil_chz = [0] * 51 

#t초까지 반복하면서, 치즈를 배열에 기록함, 배열은 51*51으로 만들어서, 각 사람이 몇번쨰 치즈를 먹었는지 기록 
for t in range(1, 101):
    #t시간에 아팠다면, 그 아픈 사람이 t시간 전까지 어떤 치즈를 먹었는지 기록 
    for i in range(s):
        if sick[i][1] == t:
            for j in range(51):
                if arr[sick[i][0]][j] == 1 :
                    # print(t)
                    # print(*arr[sick[i][0]])
                    spoil_chz[j] += 1 


    #누가 치즈를 먹었는지 기록 
    for i in range(d):
        if eat[i][2] == t:
            arr[eat[i][0]][eat[i][1]] = 1 
            # print(*arr[eat[i][0]])

#만약 t초에 어떤 사람이 아팠다면, 그 전에 그 사람이 먹었던 치즈는 모두 상했다고 판단, 그리고 마지막에 해당 치즈를 먹은 인원은 전부 약을 먹어야 하는 인원이라고 생각 

# spoil_chz = list(set(spoil_chz))
# print(spoil_chz)
chz = []
for i in range(51):
    if spoil_chz[i] == s :
        chz.append(i)


ans = 0 

# print(*chz)

for i in range(51):
    for j in chz:
        if arr[i][j] == 1 :
            ans +=1 
            break

print(ans)