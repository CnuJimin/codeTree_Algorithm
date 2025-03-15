n, k = map(int, input().split())

answer = []


def choose(cur_n):
    if cur_n > k:
        print(*answer)
        return 
    
    for i in range(1, n+1): # n = 2 , k = 2
        answer.append(i) # [1, 2]
        choose(cur_n + 1)
        answer.pop()
        answer.append(i + 1)
        answer.pop()

choose(1)