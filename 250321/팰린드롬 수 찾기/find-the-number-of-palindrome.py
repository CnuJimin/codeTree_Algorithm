x, y = map(int, input().split())

#x,y 사이의 수를 하나씩 찾아서
ans = 0 
for n in range(x, y+1):
    #해당 글자와 뒤집었을 때 글자가 같은지 확인 
    reverse_n = "".join(reversed(list(str(n))))
    # print(n)
    if str(n) == reverse_n:
        ans += 1 

print(ans)