n, b = map(int, input().split())

budget = b 

students = [tuple(map(int, input().split())) for _ in range(n)]

students.sort(key = lambda x : (x[0],x[1]))

ans = 0 

for i in range(n):
    budget = b 
    cnt = 0
    for j in range(n):
        price = students[j][0]
        delivery = students[j][1]

        if j == i :
            price //= 2 
        
        if budget - (price + delivery) >= 0 :
            cnt += 1 
            budget -= (price + delivery)
        else:
            break
    
    ans = max(ans, cnt)

print(ans)