n, m, p = map(int, input().split())
record = [tuple(input().split()) for _ in range(m)]
#p번째 부터 나머지 사람들은 다 읽었음
#n명의 사람 A~A+n명 65

arr = [False] * n

for i in range(p-1, n):
    #누가 보냈는지 확인 
    arr[ord(record[i][0]) - 65] = True 

ans = [] 

for i in range(m):
    if not arr[i]:
        ans.append(chr(i+65))


print(*ans)