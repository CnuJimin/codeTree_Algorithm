n = int(input())

def getSum(num):
    if num == 1:
        return 1
    if num == 2:
        return 2


    if num % 2 == 0:
        return num + getSum(num - 2)
    else:
        return num + getSum(num - 2)
    

print(getSum(n))