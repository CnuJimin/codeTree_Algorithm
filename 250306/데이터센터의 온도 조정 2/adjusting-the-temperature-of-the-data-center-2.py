N,C,G,H = map(int, input().split())
temp = [tuple(map(int, input().split())) for i in range(N)]

output = 0 
def get_output(t, t_a, t_b):
    if t < t_a:
        return C
    elif t_a <= t <= t_b :
        return G
    else:
        return H
answer = 0
#모든 온도의 범위(1 ~ 1000) t에 대해서 -> t
for t in range(1001):
    output = 0

    #각 기계들(N) i의 작업량를 구하고, 작업량의 합의 최댓값을 갱신한다 ->N => o(NT)
    for i in range(N):
        output += get_output(t,temp[i][0],temp[i][1])
    answer = max(answer, output)

print(answer)
