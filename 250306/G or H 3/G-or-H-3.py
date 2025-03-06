n, k = map(int, input().split())
pos = []
alp = []

for i in range(n):
    a, b = input().split()
    pos.append(int(a))
    alp.append(b)


answer = 0 

# 모든 위치 i, i + k에 대해서 
for i in range(0, 1000-k+1):
    score = 0
    start = i
    end = i + k
    #힐거 한다, N을 돌면서 해당 구역에 점수가 몇점인지 구한다. 

    for j in range(n):
        if start<= pos[j] <=end : 
            if alp[j] == 'G':
                score += 1
            else:
                score += 2
    answer = max(answer, score)

print(answer)



