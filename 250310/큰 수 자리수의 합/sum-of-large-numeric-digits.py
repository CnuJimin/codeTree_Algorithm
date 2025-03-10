a,b,c = map(int, input().split())

num = a*b*c

def getSum(num):
    if num < 10 :
        return num % 10 
    
    return getSum(num//10) + (num % 10)


print(getSum(num))
