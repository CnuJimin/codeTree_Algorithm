n = int(input())

def makeSum(num):
    if num <= 10 : 
        return num * num

    return makeSum(num//10) + (num % 10) * (num % 10)

print(makeSum(n))