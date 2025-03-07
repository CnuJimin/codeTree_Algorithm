# 모든 NNN 수에 대해서 
# 2번 카운트가 있으면 해당 숫자 중 하나가 존재함 , 1번 카운트가 존재하면 해당 자리에 숫자가 존재함 //여기까지 생각함 => 이걸 그냥 NNN에 대해서 시켜보고
# 주어진 카운트와 비교하면 되는거였음 

N = int(input())

ques = [tuple(map(int, input().split())) for i in range(N)]

cnt = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k :
                continue

            succeeded = True

            #i,j,k 라는 수과 질문한 수를 비교하기 위해 cnt_1,cnt_2를 구해서 비교함 
            for num, c1, c2 in ques:
                x,y,z = map(int, list(str(num)))

                cnt_1 = 0
                cnt_2 = 0

                #cnt_1, cnt_2를 구하기 
                if x == i:
                    cnt_1 += 1
                if y == j:
                    cnt_1 += 1
                if z == k:
                    cnt_1 += 1
                
                if x == j or x == k:
                    cnt_2 += 1
                if y == i or y == k:
                    cnt_2 += 1
                if z == i or z == j:
                    cnt_2 += 1
                
                # 만약 해당 수가 cnt_1, cnt_2 둘중 하나라도 c1,c2와 다르다면 만족하지 못하는 수임 
                if c1!= cnt_1 or c2 != cnt_2:
                    succeeded = False
                    # break
            
            if succeeded:
                cnt += 1


print(cnt)