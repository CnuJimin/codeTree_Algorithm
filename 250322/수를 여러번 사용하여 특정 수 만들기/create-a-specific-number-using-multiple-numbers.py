a, b, c = map(int, input().split())

num = 0 

ans = 0

#a를 곱할 횟수 
for i in range(1000):
    #b를 곱할 횟수 
    for j in range(1000):
        num = a * i + b * j 
    
        if num <= c :
            ans = max(ans, num)

print(ans)