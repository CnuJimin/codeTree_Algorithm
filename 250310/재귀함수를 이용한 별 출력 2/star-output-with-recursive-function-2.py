n = int(input())

def printStar(num):
    if num == 0 :
        return 
    
    print("* " * num)
    printStar(num - 1)
    print("* " * num)


printStar(n)