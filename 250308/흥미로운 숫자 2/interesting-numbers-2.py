x ,y = map(int, input().split())
#x,y 사이의 모든 숫자에 대해 
ans = 0
for i in range(x, y+1):
    cnt = 0
    num = list(str(i))
    digits = [0] * 10
    digits_num = len(num)

    for j in num:
        digits[int(j)] += 1
    
    interesing = False

    for j in range(10):
        if digits[j] == digits_num -1 : 
            interesing = True
    
    if interesing:
        ans += 1


print(ans)
#숫자가 2개 이상 다르면 숫자를 센다 