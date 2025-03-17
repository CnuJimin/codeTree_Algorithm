#서로 다른 세 수를 선택한다 
#해당 수들의 일의자리수 부터 더해서 10을 넘지 않는지 확인한다. 
#수는 최대 5자리임 
n = int(input())

nums = [int(input()) for _ in range(n)]

def splits(num):
    result = []
    result.append((num % 100000) // 10000)
    result.append((num % 10000) // 1000)
    result.append((num % 1000) // 100)
    result.append((num % 100) // 10)
    result.append((num % 10) // 1)
    return result




def isCarry(x,y,z):
    x_arr = splits(x)
    y_arr = splits(y)
    z_arr = splits(z)

    for i in range(5):
        if x_arr[i] + y_arr[i] + z_arr[i] >= 10 :
            return True 
    
    return False
    


ans = -1 

#세 수를 선택함 
for i in range(n-2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if not isCarry(nums[i], nums[j], nums[k]):
                # print(nums[i], nums[j], nums[k])
                ans = max(ans, nums[i] + nums[j] + nums[k])

print(ans)