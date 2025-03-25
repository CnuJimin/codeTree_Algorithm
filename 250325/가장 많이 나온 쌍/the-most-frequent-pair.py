#1~n까지의 수 중 2개를 선택해서, 순서 쌍 중 일치하면 횟수를 셈, 그리고 그 최댓값을 갱신함 

n, m = map(int, input().split())

pair = [list(map(int, input().split())) for _ in range(m)]

ans = 0 


for i in range(1, n+1):
    for j in range(i+1, n+1):
        num = []
        cnt = 0 


        num.append(i)
        num.append(j)

        for k in range(m):
            if num == sorted(pair[k]):
                # print(f"num = {num}, pair = {pair[k]}")
                cnt += 1
        # print(num)
    
        ans = max(ans, cnt)

print(ans)