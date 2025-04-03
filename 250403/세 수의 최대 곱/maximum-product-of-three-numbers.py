#3개를 골랐을 때 최댓값을 구할 수 있는 경우 
#1. +++, --+, 
#2. 전부 -라면 0고르기, 0이 없으면 제일 작은 값 3개 곱하기 

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

minus = 0 
zero = 0 

for i in arr:
    if i < 0 :
        minus += 1
    if i == 0 :
        zero += 1 

# -가 2개 이상존재하지 않을 때, 정렬하고 뒤에서 3개 곱하기 
if minus < 2 :
    ans = arr[-1] * arr[-2] * arr[-3]

# -가 2개 이상 존재하면 맨 뒤에서 세개 곱한거랑, 제일 작은 수 2개 제일 큰수 하나 곱한거 비교 
elif minus == n :
    if zero == 0 :
        ans = arr[-1] * arr[-2] * arr[-3]
    elif zero >= 1 :
        ans = 0

elif minus >= 2 :
    ans = max(arr[0] * arr[1] * arr[-1], arr[-1] * arr[-2] * arr[-3])
# 만약 전부 -라면 0이 존재하면 0곱하고, 없으면 제일 작은수 3개 

print(ans)

