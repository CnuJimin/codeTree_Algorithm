n = int(input())

beautyNum = [] 

#n크기 배열을 만들고.. 

ans = 0 

def beauty(num):
    global ans

    if num == n :
        ans += 1
        return 
    
    if num > n :
        return 
    
    for i in range(1, 5):
        for j in range(i):
            beautyNum.append(i)
        
        beauty(num + i)

        for j in range(i):
            beautyNum.pop()


beauty(0)


print(ans)
        