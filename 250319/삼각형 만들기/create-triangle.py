
n = int(input())

x = []
y = [] 

for _ in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)


ans = 0 
#n개의 점 중에서 세개를 선택함 
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
        #세개의 점들 중에서 y축(두번째 원소)끼리 뺐을 때 0이 되는 수가 있고, x축끼리 뺐을 때 0이되는 수가 있다면, 삼각형이 가능
            if x[i] - x[j] == 0 or x[i] - x[k] == 0 or x[j] - x[k] == 0 :
                if y[i] - y[j] == 0 or y[i] - y[k] == 0 or y[j] - y[k] == 0 :
                    ans = max(ans, (max(x[i], x[j],x[k]) - min(x[i], x[j], x[k])) * (max(y[i], y[j],y[k]) - min(y[i], y[j], y[k])))
            

print(ans)
