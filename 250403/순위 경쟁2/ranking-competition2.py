#점수를 기록해서, 점수가 더 높은 사람을 계속 추가함, 그런데 배열의 마지막과 비교해서 변화가 없다면 추가하지 않음 

n = int(input())

arr = ["AB"]

score = [0, 0]

# game = [tuple(input().split()) for _ in range(n)]

for i in range(n):
    who, point = input().split()
    point = int(point)

    who = ord(who) - 65

    score[who] += point

    if score[0] > score[1] and arr[-1] != "A":
        arr.append("A")
    elif score[0] < score[1] and arr[-1] != "B":
        arr.append("B")
    elif score[0] == score[1] and arr[-1] != "AB":
        arr.append("AB")

print(len(arr) - 1)


