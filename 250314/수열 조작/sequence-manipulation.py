from collections import deque 

n = int(input())
dq = deque()

#1~n까지 정수를 deque에 추가 
for i in range(1, n + 1):
    dq.append(i)

#deque에 정수 하나만 남을 때 까지 반복 
while len(dq) != 1 :
    #deque의 맨 앞 수를 제거 
    dq.popleft()
    #그 후 맨 앞의 수를 맨 뒤로 이동 
    dq.append(dq[0])
    dq.popleft()

#deque에 마지막 남은 수 출력 
print(dq.pop())