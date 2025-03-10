n = int(input())

def flower(num):
    if num == 0 :
        return 
    
    print(num, end = " ")
    flower(num - 1)
    print(num, end = " ")

flower(n)
