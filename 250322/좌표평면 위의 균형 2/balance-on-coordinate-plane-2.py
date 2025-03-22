import sys

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

#두개의 선을 선택함 
for x_line in range(0, 101, 2):
    for y_line in range(0, 101, 2):
        a,b,c,d = 0, 0, 0, 0

        for x,y in points:
            if x > x_line and y > y_line:
                a += 1
            if x < x_line and y > y_line:
                b += 1
            if x < x_line and y < y_line:
                c += 1
            if x > x_line and y < y_line:
                d += 1
        
        # print(f"x축 : {x_line}, y축: {y_line} => A: {a}, B: {b}, C: {c}, D: {d}")
        m = max(a,b,c,d)
    
        ans = min(m, ans)

print(ans)

