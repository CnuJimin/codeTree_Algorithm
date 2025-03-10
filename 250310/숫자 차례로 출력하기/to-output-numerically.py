n = int(input())


def printNum(num):
    if num == 0:
        return 
    
    printNum(num-1)
    print(num, end = " ")

def reversePrintNum(num):
    if num == 0 : 
        return 
    
    print(num, end = " ")
    reversePrintNum(num-1)


printNum(n)
print()
reversePrintNum(n)
    
