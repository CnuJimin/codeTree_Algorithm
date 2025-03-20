#n 개의 선분 중에서 3개를 선택하지 않기 
 
n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            arr = [0] * 101
            flag = True
            for l in range(n):
                if l == i or l == j or l == k :
                    continue
                
                a,b = lines[l]

                for o in range(a, b+1):
                    arr[o] += 1
            
            for l in arr:
                if l > 1 :
                    flag = False
            
            if flag:
                ans += 1

print(ans)