n = int(input())

def arrNum(num):
    if num == 1:
        return 2 
    if num == 2:
        return 4
    return (arrNum(num-1) * arrNum(num-2)) % 100 

print(arrNum(n))