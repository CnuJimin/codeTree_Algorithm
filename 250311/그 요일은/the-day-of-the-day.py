m1 ,d1, m2, d2 = map(int, input().split())
week_of_day = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(len(day)):
    if week_of_day == day[i] :
        week_of_day = i


total_day1 = 0
total_day2 = 0


for i in range(m1):
    total_day1 += month[i]

total_day1 += d1 

for i in range(m2):
    total_day2 += month[i]

total_day2 += d2


diff = total_day2 - total_day1

answer = 0
answer += diff // 7 
rest_day = diff % 7

if rest_day < week_of_day :
    print(answer)
else:
    print(answer + 1)


