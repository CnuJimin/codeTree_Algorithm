n, k = map(int, input().split())
candy = [tuple(map(int, input().split())) for i in range(n)] #[사탕의 개수, 바구니 위치]

# --그냥 완전 탐색 -- 
# answer = 0
# # 모든 경우에 대해 / 모든 c위치에 대해서 
# for c in range(101):
#     # [c-k, c+k]구간 사이에 사탕의 개수를 찾고, 최댓값을 갱신한다
#     st = c - k if c - k >= 0 else 0
#     end = c + k
#     cnt = 0 
#     for i in range(n):
#         if st<= candy[i][1] <= end :
#             cnt += candy[i][0]
#         answer = max(answer, cnt)

# print(answer)


# -- 카운팅 어레이 -- 
arr = [0] * 101
answer = -1 

for i in range(n):
    arr[candy[i][1]] += candy[i][0]

# for i in range(101):
#     st = i - k if i - k >= 0 else 0
#     end = i + k if i + k <= 100 else 100
#     answer = max(answer, sum(arr[st : end + 1]))
    
for i in range(k, 100 - k + 1):
    answer = max(answer, sum(arr[i - k : i + k -1]))


print(answer)

