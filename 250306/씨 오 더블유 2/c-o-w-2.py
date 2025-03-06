N = int(input())
cow = input()

cnt = 0
#그 i +1 부터 j에 대해 o를 찾고, j+1부터 k에 대해 w를 찾아서 수를 셈 
#cow의 각 자리 글자 i에 대해서 c를 찾고
for i in range(N):
    for j in range(i + 1 , N):
        for k in range(j + 1, N):
            if cow[i] == 'C' and cow[j] == 'O' and cow[k] == 'W':
                cnt += 1

print(cnt)