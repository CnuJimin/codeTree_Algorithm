n = int(input())

cnt = 0

def untilOne(num):
    global cnt 
    if num == 1 :
        return 
    
    if num % 2 == 0 :
        num //= 2 
    else:
        num //= 3 
    
    cnt += 1

    untilOne(num)

untilOne(n)

print(cnt)