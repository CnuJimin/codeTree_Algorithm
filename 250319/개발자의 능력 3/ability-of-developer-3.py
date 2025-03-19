import sys

#6명의 개발자중 3개를 골라서, 전체 합에서 두번 뺸 값의 절댓값이 최소가 되도록 함 

ability = list(map(int, input().split()))

total = sum(ability)

ans = sys.maxsize

#3명을 선택
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            ans = min(ans, abs(total - 2 * (ability[i] + ability[j] + ability[k])))

print(ans)