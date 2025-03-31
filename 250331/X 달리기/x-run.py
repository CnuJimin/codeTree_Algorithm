import sys

x = int(input())

dist = 0 
time = 0 
speed = 0

while True:
    time += 1
    if x - dist > (speed+1) * (speed + 2) // 2:
        speed += 1
    elif x - dist < (speed) * (speed + 1) // 2 :
        speed -= 1
    
    dist += speed

    if dist == x :
        break

print(time)





#속도를 높일지, 유지할지, 줄일지 결정하는 방법 
#남은 거리가 현재 속도 +1 부터 1까지 더한 값 보다 크면 상승
#남은 거리가 현재 속도 부터 1까지 더한 값 보다 크면 그대로 
# 남은 거리가 현재 속도부터 1까지 더한 값보다 작으면 하락 

# 현재 속도를 유지할 때 도착하는 순간 속력이 1이면서 도착할 수 있는가? 
# 현재 속도를 계속 더했을 때 