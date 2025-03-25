n = int(input())
scope = [tuple(map(int, input().split())) for _ in range(n)]

#처음 x의 범위 
for i in range(scope[0][0]// 2 , scope[0][1]//2 + 1 ):
    x = i 
    flag = True 
    for j in range(n):
        x *= 2 
        if scope[j][0] <= x <= scope[j][1]:
            continue
        else:
            flag = False
    
    if flag:
        print(i)
        break