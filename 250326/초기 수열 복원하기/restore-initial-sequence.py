n = int(input())
arr = list(map(int, input().split()))
visited = [0] * (n+1)
result = []
#1~n까지 수 중에 2개를 골라서 합이 되는 경우를 n-1번 확인 

#처음 들어갈 수를 일단 고름
for i in range(1,n+1):
    result = []
    result.append(i)
    visited[i] = 1
    flag = True
    # print("초기 reuslt = " , *result)
    for j in range(n-1):
        #그 다음수를 고름 
        for k in range(1, n+1):
            if visited[k] != 1:
                if result[-1] + k == arr[j]:
                    result.append(k)

                    # print("몇번째 arr = ", j, "값 추가, ", *result)
                    visited[k] = 1
                    flag = False
                    if len(result) == n :
                        print(*result)
                    break
        
        if flag:
            visited = [0] * (n+1)
            break



            


        