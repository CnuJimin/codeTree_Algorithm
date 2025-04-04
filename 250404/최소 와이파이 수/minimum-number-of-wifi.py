#와이파이를 어디에 둬야할까? 
#m부터 이동하면서 거기에 와이파이 기계를 두고, 쭉 이동, 
#만약 맨 왼쪽 인덱스에 1이고 와이파기 통하지 않는 집이 있으면 무조건 두고, 그게 아니라면 한칸 더 이동 

n, m = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False] * 300


ans = 0 

if m == 0 :
    for i in arr:
        if i == 1 :
            ans += 1
else:
    for i in range(m, n-m+1):
        if arr[i-m] == 1 and visited[i-m] == False:
            ans += 1
            for j in range(i-m, i+m+1):
                visited[j] = True

print(ans)
