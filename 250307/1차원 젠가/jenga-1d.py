n = int(input())
blcoks = [int(input()) for i in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

s1, e1 = s1 -1, e1- 1
s2, e2 = s2 -1, e2- 1

s = [s1,s2]
e = [e1,e2]

for t in range(2):
    temp = []
    #블록 s,e의 범위를 0으로 만든다
    for i in range(s[t], e[t] + 1): 
        blcoks[i] = 0

    #블록 배열을 돌면서 0이 아니면 temp 배열에 추가한다 
    for i in range(len(blcoks)):
        if blcoks[i] != 0:
            temp.append(blcoks[i])
    #temp를 block에 복사한다. 

    blcoks = temp
    # print(*blcoks)


print(len(blcoks))
for i in blcoks:
    if i != 0 :
        print(i)