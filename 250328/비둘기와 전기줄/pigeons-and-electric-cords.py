# 각 비둘기의 관찰 횟수와, 위치를 나타내는 배열을 두개 생성
# 비둘기를 관찰할 때마다 횟수 배열에 +1, 횟수가 2인 비둘기부터는, 현재 위치와 관찰된 위치가 다르다면 건넌 것으로 체크 

n = int(input())

dected = [tuple(map(int, input().split())) for _ in range(n)]

num = [0] * 11 # 관찰 횟수 배열 
pos = [0] * 11 # 관찰된 위치 배열 

ans = 0
for i in range(n):
    who, line = dected[i]

    #만약 해당 비둘기가 2번 이상 발견됐고, 위치가 바뀌었다면 체크 
    if num[who] >= 1 and pos[who] != line:
        # print(who,"번째 비둘기가", line,"으로 건넜음")
        ans += 1
    #관찰 횟수 추가, 위치 최신화 
    num[who] += 1
    pos[who] = line
    # print("비둘기 관찰 횟수")
    # print(*num)
    # print("비둘기 위치")
    # print(*pos)


print(ans)