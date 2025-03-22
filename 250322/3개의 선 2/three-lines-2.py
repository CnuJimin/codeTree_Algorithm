#일단 선 3개를 선택하는 법 x,y 범위는 0~10 
#x3개, y0개, ... x0개 y3개 선택한다고 하고 
#해당 선분 위에 좌표가 있는지 파악하려면, x,y따로 배열 만들고, 이를 set으로 중복 없이 해둠, 그리고 선택한 선분의 좌표에 이것들이 있는지 확인해보자 

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0 

for i in range(11):
    for j in range(11):
        for k in range(11):
            scucess = True 
            for x,y in points:
                if x == i or x == j or x == k:
                    continue 
                
                scucess = False
            
            if scucess:
                ans = 1 


            scucess = True 
            for x,y in points:
                if x == i or x == j or y == k:
                    continue 
                
                scucess = False
            if scucess:
                ans = 1            
            
            
            scucess = True 
            for x,y in points:
                if x == i or y == j or y == k:
                    continue 
                
                scucess = False
            
            if scucess:
                ans = 1   


            scucess = True
            for x,y in points:
                if y == i or y == j or y == k:
                    continue 
                
                scucess = False
            
            if scucess:
                ans = 1 

print(ans)