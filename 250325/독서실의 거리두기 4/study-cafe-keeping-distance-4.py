n = int(input())
arr = list(map(int,list(input())))

ans = 0 
#0인 곳에 일단 좌석을 배치하고, 거리간의 차이를 구함 
for i in range(n):
    if arr[i] == 0 :
        arr[i] = 1 
        for j in range(i+1, n):
            if arr[j] == 0 :
                arr[j] = 1
            
            #거리 구하기 
            for k in range(n):
                for l in range(k+1, n):
                    if arr[k] == 1 and arr[l] == 1 :
                        dist = l - k 
                    
                    ans = max(ans, dist)
                    break


            arr[j] = 0 
    
    arr[i] = 0 

print(ans)