N = int(input())
a,b,c = map(int, input().split())

count = 0 
#모든 NNN 에 대해 -> N^3
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            #a,b,c와 2 이내인 수가 하나라도 있으면 수를 센다 
            if abs(a-i) <= 2 or abs(b-j) <= 2 or abs(c - k) <= 2 :
                count +=1
print(count)