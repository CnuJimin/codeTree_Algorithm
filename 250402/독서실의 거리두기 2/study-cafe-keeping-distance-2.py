import sys
#양 끝에 1이 확정이 아니라서, 만약 양 끝이 0이라면 양 끝에 1을 뒀을 때의 경우를 고려해야 함 
n = int(input())

arr = list(map(int, list(input())))

# 만약 최대거리보다 1을 둔게 더 크면 거기다 1을 두고 아니면 가운데 최대거리를 둠 

#좌석을 돌면서, 최대 거리인 곳을 찾고, 좌우 자리 위치를 기록해둠, 

x,y = 0,0
dist = 0  
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == 1 and arr[j] == 1 :
            if j - i > dist:
                dist = j - i
                x,y = i, j 
            break

#첫번째 1과 마지막 1위치 
first, last = 0, 0 
for i in range(0, n):
    if arr[i] == 1 :
        first = i
        break

for i in range(n-1, 0, -1):
    if arr[i] == 1 :
        last = i 
        break

# print(last)

#근데 맨 왼쪽 혹은 오른쪽에 0이 존재하면 최대거리(만약 홀수이면 //2, 짝수이면 //2 + 1)와 좌우에 1을 뒀을때 크기를 비교해서 
if arr[0] == 0 or arr[-1] == 0 :
    if first-1 >= n - last - 1 :
        if first - 1 > dist // 2 if dist % 2 == 0 else dist // 2 + 1:
            arr[0] = 1 
        else:
            arr[(x+y) // 2 ] = 1

    else:
        # print("dist = ", dist)
        # print("last= ", last)
        if n - last - 1 > dist // 2 :
            arr[-1] = 1
        else:
            arr[(x+y) // 2 ] = 1


else:
    arr[(x+y) // 2 ] = 1

# print(x,y)
# print(*arr)

ans = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == 1 and arr[j] == 1 :
            if j - i < ans:
                ans = j - i
            break

print(ans)



# dist.sort()

# if len(dist) == 0 :
#     print(1)

# elif arr[0] == 0 :
#     if first > dist[-1]//2 and dist[-1] % 2 == 0 :
#         print(min(first-1, min(dist)))
#     elif first > dist[-1]//2 + 1 and dist[-1] % 2 != 0 :
#         print(min(first, min(dist)))
#     else:
#         div = dist[-1]//2
#         if dist[-1] % 2 == 0 :
#             dist[-1] = div
#             dist.append(div)
#             print(min(dist))
#         else:
#             dist[-1] = div + 1
#             dist.append(div)
#             print(min(dist))



# elif arr[-1] == 0 :
#     if n-last > dist[-1]//2 and dist[-1] % 2 == 0:
#         print(min(n-last-1, min(dist)))
#     elif n-last > dist[-1]//2 + 1 and dist[-1] % 2 == 0 :
#         print(min(n-last-1, min(dist)))

#     else:
#         div = dist[-1]//2
#         if dist[-1] % 2 == 0 :
#             dist[-1] = div
#             dist.append(div)
#             print(min(dist))
#         else:
#             dist[-1] = div + 1
#             dist.append(div)
#             print(min(dist))

# else:
#     div = dist[-1]//2
#     if dist[-1] % 2 == 0 :
#         dist[-1] = div
#         dist.append(div)
#         print(min(dist))
#     else:
#         dist[-1] = div + 1
#         dist.append(div)
#         print(min(dist))


