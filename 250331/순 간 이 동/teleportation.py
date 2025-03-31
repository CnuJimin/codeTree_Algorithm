a,b,x,y = map(int, input().split())

#A->B 바로 이동
#A->x->y->B
#A->y->x->B

print(min(abs(a-b), abs(a-x)  + abs(b-y), abs(a-y)  + abs(b-x)))