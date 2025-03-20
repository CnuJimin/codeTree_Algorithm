n, m, d, s = map(int, input().split())

class Info_1:
    def __init__(self, p, m, t):
        self.p = p 
        self.m = m
        self.t = t 


class Info_2:
    def __init__(self, p,t):
        self.p = p 
        self.t = t 

inf_1 = []
for i in range(d):
    p,m,t = tuple(map(int, input().split()))
    inf_1.append(Info_1(p,m,t))

inf_2 = []
for i in range(s):
    p,t = tuple(map(int, input().split()))
    inf_2.append(Info_2(p,t))

ans = 0 

for i in range(1, m+1):
    time = [0] * (n+1)

    for info_1 in inf_1:
        if info_1.m != i :
            continue
        
        p = info_1.p

        if time[p] == 0 :
            time[p] = info_1.t
        elif time[p] > info_1.t:
            time[p] = info_1.t
        
    
    possible = True 

    for info_2 in inf_2:
        person = info_2.p

        if time[person] == 0 :
            possible = False
        
        if time[person] >= info_2.t:
            possible = False
    
    pill = 0 

    if possible :
        for i in range(1, n+1):
            if time[i] != 0 :
                pill += 1
        
        ans = max(ans, pill)


print(ans)