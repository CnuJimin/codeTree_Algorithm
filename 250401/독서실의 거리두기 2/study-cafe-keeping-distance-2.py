#양 끝에 1이 확정이 아니라서, 만약 양 끝이 0이라면 양 끝에 1을 뒀을 때의 경우를 고려해야 함 
n = int(input())

arr = list(map(int, list(input())))

#일단 좌석 간의 거리를 구하고, 마지막에 앞에 0일 경우, 
#뒤에 1일 경우 거리를 구한다음, 만약 그 거리가 최대 거리보다 길다면, 그냥 최솟값 구하면 되고, 
# 최대 거리보다 짧으면 그냥 원래대로 진행하면 됨 

dist = []
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == 1 and arr[j] == 1 :
            dist.append(j - i)
            break

# print(*dist)

#첫번째 1과 마지막 1위치 
first, last = 0, 0 
for i in range(n):
    if arr[i] == 1 :
        first = i 
        break

for i in range(n-1, 0, -1):
    if arr[i] == 1 :
        last = i 
        break

dist.sort()

if len(dist) == 0 :
    print(0)

elif arr[0] == 0 :
    if first > dist[-1]//2:
        print(first-1)
    else:
        div = dist[-1]//2
        if dist[-1] % 2 == 0 :
            dist[-1] = div
            dist.append(div//2)
            print(min(dist))
        else:
            dist[-1] = div + 1
            dist.append(div)
            print(min(dist))


elif arr[-1] == 0 :
    if n-last > dist[-1]//2:
        print(n-last-1)
    else:
        div = dist[-1]//2
        if dist[-1] % 2 == 0 :
            dist[-1] = div
            dist.append(div)
            print(min(dist))
        else:
            dist[-1] = div + 1
            dist.append(div)
            print(min(dist))

else:
    div = dist[-1]//2
    if dist[-1] % 2 == 0 :
        dist[-1] = div
        dist.append(div)
        print(min(dist))
    else:
        dist[-1] = div + 1
        dist.append(div)
        print(min(dist))


