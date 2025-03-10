n = int(input())

def cntNum(num):
    if num == 1:
        return 0
    
    

    if num % 2 == 0:
        return cntNum(num//2) + 1
    else:
        return cntNum(num * 3 + 1) + 1

print(cntNum(n))