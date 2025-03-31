import sys

x = int(input())
#매 시간마다 시간을 줄일 것인지 높일 것인지, 유지할 것인지 판단? => 이건 어떻게 구현할지 모르겠음
#그냥 x 시간 중에 시간 하나를 정해서, 그 시간부터 속도를 줄인다고 생각해보자 

#거리가 x -1 이면 그냥 속도 유지 

ans = sys.maxsize
#i 시간부터 속도를 줄임 만족했을 때 break 문을 안걸면 시간초과 
for i in range(1, x):
    # print(f"======변곡점{i}========")
    #속도를 유지할 구간 
    for k in range(i+1, x):
        for l in range(k+1, x):
            dist = 0 
            time = 0 
            speed = 0

            for j in range(1, x):
                if j >= i :
                    #j가 k와 l 사이일 때는 속도를 유지함 
                    if  k<= j <= l:
                        time += 1
                        dist += speed
                        if dist == x and speed == 1:
                            ans = min(ans, time)
                    else:
                        #속도를 줄여야함 
                        time += 1
                        speed -= 1
                        dist += speed
                        if dist == x and speed == 1 :
                            ans = min(ans, time)
                else:
                    speed += 1 
                    dist += speed
                    time += 1
                
                if speed <= 0 :
                    break
                


        # print(f"time = {j} 속도 = {speed} 거리 = {dist}" )

print(ans)


