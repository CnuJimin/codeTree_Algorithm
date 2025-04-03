# 두번째로 작은 수를 구하는 방법 
# 배열을 정렬시키고, 가장 작은 값보다 큰 값이 가장 먼저 나온 수가 2번째로 작은 수 
# 원래 배열에서 그 수의 인덱스를 구하고 거기에 +1을 하면 정답 

n = int(input())

arr = list(map(int, input().split()))

sort_arr = sorted(arr)
min_value = sort_arr[0]
find_value = 0 

for i in range(n):
    if sort_arr[i] > min_value :
        find_value = sort_arr[i]
        break

cnt = 0 

for i in range(n):
    if arr[i] == find_value:
        cnt += 1
        ans = i

# print(find_value)


if find_value == 0 or cnt > 1 :
    print(-1)
else:
    print(ans + 1)
    