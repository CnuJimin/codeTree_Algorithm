n, m, p = map(int, input().split())
record = [tuple(input().split()) for _ in range(m)]
# print(*record)
#p번째 부터 나머지 사람들은 다 읽었음
#n명의 사람 A~A+n명 65

arr = [False] * (n)

for i in range(p-1, m):
    #누가 보냈는지 확인 
    # print(ord(record[i][0]))
    arr[ord(record[i][0]) - 65] = True 



# 반복문 돌면서 자기이전에 자기랑 남아 있는 수가 같았던 사람은 뻄 
for i in range(m):
    if record[p-1][1] == record[i][1]:
        arr[ord(record[i][0]) - 65] = True

# print(*arr)


ans = [] 

for i in range(n):
    if not arr[i]:
        ans.append(chr(i+65))

        


if record[p-1][1] == "0" :
    print("")
else:
    print(*ans)