n = int(input())

def strange(num):
    if num == 1 :
        return 1
    if num == 2:
        return 2 
    
    return strange(num//3) + strange(num-1)

print(strange(n))