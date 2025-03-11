n = int(input())

def beTen(num):
    num = list(map(int, list(str(num))))

    output = 0
    for i in range(len(num)):
        output = output * 2 + num[i]
    
    return output

def beTwo(num):
    arr = []

    while True:
        if num < 2 :
            arr.append(num)
            break
        
        arr.append(num % 2)
        num //= 2
    
    return arr

n = 17 * beTen(n)

answer = beTwo(n)

for i in answer[::-1]:
    print(i, end = "")
