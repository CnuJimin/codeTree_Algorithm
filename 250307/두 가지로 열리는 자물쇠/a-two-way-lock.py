N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

#모든 자리에 대해 조건을 만족하면 숫자를 셈 

count = 0


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if(abs(a1 - i) <= 2 or abs(a1 - i)>= N - 2) and (abs(b1 - j) <= 2 or abs(b1 - j)>= N - 2) and(abs(c1 - k) <= 2 or abs(c1 - k)>= N - 2) :
                count += 1
            elif (abs(a2 - i) <= 2 or abs(a2 - i)>= N - 2) and (abs(b2 - j) <= 2 or abs(b2 - j)>= N - 2) and(abs(c2 - k) <= 2 or abs(c2 - k)>= N - 2) :
                count += 1

print(count)