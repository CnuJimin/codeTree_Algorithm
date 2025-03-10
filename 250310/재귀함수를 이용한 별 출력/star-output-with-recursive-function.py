n = int(input())

def printStar(num):
    if num == 0 :
        return 
    
    printStar(num - 1)
    print("*" * num)


printStar(n)