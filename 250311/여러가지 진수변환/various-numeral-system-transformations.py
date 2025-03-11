num, n = map(int, input().split())

answer = []

while True:
    # print(num)

    if num < n :
        answer.append(num)
        break
    
    answer.append(num % n)
    num //= n

for i in answer[::-1]:
    print(i, end = "")