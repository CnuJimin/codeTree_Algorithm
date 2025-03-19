# 6명을 2,2,2로 나눠야함.. 
import sys
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(6):
    for j in range(6):
        if j == i :
            continue
        for k in range(6):
            if k == i or k == j:
                continue 
            for l in range(6):
                if l == k :
                    continue
                team_1 = arr[i] + arr[j]
                team_2 = arr[k] + arr[l]
                team_3 = sum(arr) - team_1 - team_2

                ans = min(ans, max(team_1, team_2, team_3) - min(team_1, team_2, team_3))

print(ans)