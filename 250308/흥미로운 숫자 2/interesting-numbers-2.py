x ,y = map(int, input().split())
#x,y 사이의 모든 숫자에 대해 
cnt = 0
for i in range(x, y+1):
    num = list(str(i))
    if len(num) - len(set(num)) == 1:
        cnt += 1

print(cnt)
#숫자가 2개 이상 다르면 숫자를 센다 