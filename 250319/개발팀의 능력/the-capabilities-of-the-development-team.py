import sys

arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(5):
    for j in range(5):
        if i == j :
            continue 
        for k in range(5):
            if k == i or k == j :
                continue 
            for l in range(5):
                if l == k or l == j or l == i :
                    continue
                
                team_1 = arr[i] + arr[j]
                team_2 = arr[k] + arr[l]
                team_3 = sum(arr) - team_1 - team_2

                if team_1 == team_2 or team_1 == team_3 or team_2 == team_3:
                    continue 
                
                ans = min(ans, (max(team_1, team_2, team_3) - min(team_1, team_2, team_3)))


if ans == sys.maxsize:
    print(-1)
else:
    print(ans)