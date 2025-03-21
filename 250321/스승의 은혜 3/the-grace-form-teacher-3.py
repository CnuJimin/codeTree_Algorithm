n, b = map(int, input().split())

students = [tuple(map(int, input().split())) for _ in range(n)]
students.sort(key = lambda x : x[0] + x[1])


normal_budget = b 
normal_count = 0 
prices = [p+b for p,b in students]

for price in prices:
    if normal_budget >= price :
        normal_budget -= price
        normal_count += 1
    else:
        break

ans = 0 
max_count = 0 

for i in range(n):
    temp_budget = b - (students[i][0]//2 + students[i][1])
    temp_count = 1 if temp_budget >=0 else 0 

    for j in range(n):
        if i == j :
            continue
        
        price = students[j][0] + students[j][1]

        if temp_budget >= price:
            temp_budget -= price
            temp_count += 1
        else:
            break
    
    max_count = max(max_count, temp_count)

ans = max(normal_count, max_count)

print(ans)
