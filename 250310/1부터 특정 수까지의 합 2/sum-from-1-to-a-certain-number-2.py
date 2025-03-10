n = int(input())

def makeSum(num):
    if num == 0:
        return 0
    return num + makeSum(num - 1)

print(makeSum(n))