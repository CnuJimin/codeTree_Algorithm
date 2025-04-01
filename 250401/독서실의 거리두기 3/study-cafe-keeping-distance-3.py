n = int(input())

arr = list(map(int, list(input())))

#좌석 간의 거리를 배열에 넣어두고, 그 최댓값이 배열에 몇개 있는지 찾아보기 

dist = []


for i in range(n):
    for j in range(i+1, n):
        if arr[i] == 1 and arr[j] == 1 :
            dist.append(j-i)
            break




# print(*dist)

dist.sort()

if dist[-1] % 2 == 0 :
    div = dist[-1]//2
    dist[-1] = div
    dist.append(div)
else:
    div = dist[-1]//2
    dist[-1] = div + 1
    dist.append(div)

print(min(dist))


# ans = 0

# for i in dist:
#     if i == value:
#         ans+= 1

# if value % 2 == 0 :
#     print(ans)

# else:
#     print(ans * 2)