n, k, p, t = map(int, input().split())
#77 18 60 144

#N명의 개발자가 있고, 최초 전염병에 걸린 개발자는 p개발자이고,k번 악수의 악수까지만 전염병이 걸림, t번에 걸쳐 악수를 진행 

developer = [0] * (n)  # 0번 인덱스는 마지막에 재껴줘야 함 

#각 개발자마다 두번만 감염시킬 수 있음 
spread_nun = [0] * (n)

#p번 개발자 최초 감염자 
developer[p-1] = 1

handshake = []

#t번동안 반복하면서, 악수 리스트에 tuple로 t,x,y를 넣음
for _ in range(t):
    handshake.append(tuple(map(int, input().split())))

#t를 기준으로 오름차순 정렬함 
handshake.sort(key = lambda x : x[0])
# print(*handshake)

#악수 리스트를 처음부터 돌면서 x,y를 비교함, 만약 둘중 하나가 1이면 다른 한쪽도 1로 만듦, 그런데 악수 횟수를 k번까지 진행해야 함을 체크 

for t, x, y in handshake:

    #한 개발자만 감염에 걸린 경우 
    if developer[x-1] == 1 and developer[y-1] != 1:
        #감염된 개발자가 아직 k번 감염시키지 않았다면 감염시킴 
        if spread_nun[x-1] <= k :
            developer[y-1] = 1 
            spread_nun[x-1] += 1

    if developer[x-1] != 1 and developer[y-1] == 1:
        #감염된 개발자가 아직 k번 감염시키지 않았다면 감염시킴 
        if spread_nun[y-1] <= k :
            developer[x-1] = 1 
            spread_nun[y-1] += 1
    
    #둘다 감염된 경우 
    if developer[x-1] == 1 and developer[y-1] == 1 :
        spread_nun[x-1] += 1 
        spread_nun[y-1] += 1

        


for i in range(n):
    print(developer[i], end = "")


