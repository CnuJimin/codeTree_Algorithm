import sys

n = int(input())
seats = list(map(int, list(input())))

#모든 좌석을 고려함, 그런데 그 자리 왼쪽, 오른쪽에 1이 있으면 안됨,
#해당 자리에 앉았을 때 다른 1과의 거리의 최솟값을 갱신하고, 이 값의 최댓값을 갱신해서 답으로 함 

ans = 0 

for i in range(1, n):
    if i == n-1:
        if seats[i] == 1 or seats[i-1] == 1 :
            continue 
    elif seats[i - 1] == 1 or seats[i] == 1 or  seats[i + 1] == 1 :
        continue 
    
    seats[i] = 1 
    # print(*seats)
    result = sys.maxsize

    #1들간의 거리를 구함 
    for j in range(n):
        for k in range(j+1, n):
            if seats[j] == 1 and seats[k] == 1 :
                dist = abs(j-k)
                print(f"좌석{j}, {k} , 거리 = {dist}")

                break
        #거리 갱신 
        result = min(result, dist)

        # print(f"{i} 위치에 1을 넣었을 때, 1들간의 거리 => {j} , {k}, {dist}")

        continue
    
    seats[i] = 0 
    ans = max(ans, result)



print(ans)