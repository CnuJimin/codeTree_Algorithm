#처음에 0, 점수를 기록하고, 매번 가장 높은 사람을 확인한 뒤, 변화가 있으면 추가 

n = int(input())

score = [0,0,0]

arr = ["ABC"]

for i in range(n):
    who, point = input().split()
    point = int(point)
    who = ord(who) - 65

    score[who] += point

    if score[0] ==score[1] == score[2] and arr[-1] != "ABC":
        arr.append("ABC")
    elif score[0] > max(score[1], score[2]) and arr[-1] != "A":
        arr.append("A")
    elif score[0] == score[1] > score[2] and arr[-1] != "AB":
        arr.append("AB")
    elif score[0] == score[2] > score[1] and arr[-1] != "AC":
        arr.append("AC")
    elif score[1] == score[2] > score[0] and arr[-1] != "BC":
        arr.append("BC")
    elif score[1] > max(score[0], score[2]) and arr[-1] != "B":
        arr.append("B")
    elif score[2] > max(score[1], score[0]) and arr[-1] != "C":
        arr.append("C")


print(len(arr) - 1)