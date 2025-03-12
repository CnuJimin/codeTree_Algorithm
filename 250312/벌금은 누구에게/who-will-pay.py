n, m, k = map(int, input().split())

students = [0] * n 

find = False

answer = -1 

for i in range(m):
    who = int(input())

    students[who - 1] += 1

    for j in range(n):
        if students[j] >= k :
            find = True
            answer = j + 1
            break

    if find:
        print(answer)
        break


    
