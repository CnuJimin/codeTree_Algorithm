n, k, p, t = map(int, input().split())

#N명의 개발자가 있고, 최초 전염병에 걸린 개발자는 p개발자이고,k번 악수의 악수까지만 전염병이 걸림, t번에 걸쳐 악수를 진행 

developer = [0] + [0] * (n)  # 0번 인덱스는 마지막에 재껴줘야 함 

#p번 개발자 최초 감염자 
developer[p] = 1

handshake = []

#t번동안 반복하면서, 악수 리스트에 tuple로 t,x,y를 넣음
for _ in range(t):
    handshake.append(tuple(map(int, input().split())))

#t를 기준으로 오름차순 정렬함 
handshake.sort(key = lambda x : x[0])

#악수 리스트를 처음부터 돌면서 x,y를 비교함, 만약 둘중 하나가 1이면 다른 한쪽도 1로 만듦, 그런데 악수 횟수를 k번까지 진행해야 함을 체크 

cnt = 0
for t, x, y in handshake:
    if cnt > k :
        break

    if developer[x] == 1 or developer[y] == 1:
        developer[x], developer[y] = 1, 1
    cnt += 1


for i in range(n):
    print(developer[i], end = "")