n = int(input())
pos = []
char = []

for i in range(n):
    a, b = tuple(map(str, input().split()))
    pos.append(int(a))
    char.append(b)

counting_arr = [0] * 101
for i in range(n):
    counting_arr[pos[i]] = char[i]



answer = 0 
# 각 위치 i에서 범위 k에 대해 검사를 실시함 
for i in range(101):
    for j in range(i+1, 101):
        # 이 부분을 생각 못함, i와 j 위치에 사람이 있는지 확인하는 작업. 이걸 확인 안하면 g와 h의 개수가 0인 경우가 너무 많음 
        if counting_arr[i] == 0 or counting_arr[j] == 0:
            continue

        cnt_h = 0
        cnt_g = 0
        for k in counting_arr[i:j + 1]:
            if k == "G":
                cnt_g += 1
            elif k == "H":
                cnt_h += 1

        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            answer = max(answer, j-i)

# 그 범위 안에 
print(answer)