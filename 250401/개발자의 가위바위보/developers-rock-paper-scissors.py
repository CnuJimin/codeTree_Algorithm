n = int(input())

play = [tuple(map(int, input().split())) for _ in range(n)]

def game(x,y):
    if x == "주먹" and y == "가위":
        return True
    elif x == "주먹" and y == "보":
        return False
    elif x == "가위" and y == "주먹":
        return False
    elif x == "가위" and y == "보":
        return True
    elif x == "보" and y == "주먹":
        return True
    elif x == "보" and y == "가위":
        return False

ans = 0 
#주먹 가위 보 
mapping = [0, "주먹", "가위", "보"]
cnt = 0 

for i in range(n):

    a, b = play[i]
    if game(mapping[a], mapping[b]):
        cnt += 1

ans = max(cnt, ans)


#주먹 보 가위 
mapping = [0, "주먹", "보", "가위"]
cnt = 0 

for i in range(n):

    a, b = play[i]
    if game(mapping[a], mapping[b]):
        cnt += 1

ans = max(cnt, ans)
#보 주먹 가위 
mapping = [0, "보", "주먹", "가위"]
cnt = 0 

for i in range(n):
    a, b = play[i]
    if game(mapping[a], mapping[b]):
        cnt += 1

ans = max(cnt, ans)
cnt = 0 

#보 가위 주먹 
mapping = [0, "보", "가위", "주먹"]
for i in range(n):

    a, b = play[i]
    if game(mapping[a], mapping[b]):
        cnt += 1

ans = max(cnt, ans)
#가위 보 주먹 
mapping = [0, "가위", "보", "주먹"]
cnt = 0 

for i in range(n):

    a, b = play[i]
    if game(mapping[a], mapping[b]):
        cnt += 1

ans = max(cnt, ans)
#가위 주먹 보 
mapping = [0, "가위", "주먹", "보"]
cnt = 0 

for i in range(n):

    a, b = play[i]
    if game(mapping[a], mapping[b]):
        cnt += 1

ans = max(cnt, ans)

print(ans)