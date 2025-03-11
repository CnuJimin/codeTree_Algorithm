a, b = map(int, input().split())

num = int(input()) # a진수로 표현됨 

#10진수로 바꾸기 
num = list(map(int, list(str(num))))

ten_num = 0 

for i in range(len(num)):
    ten_num = ten_num * a + num[i]

num = ten_num
#다시 b 진수로 바꾸기 

answer = []
while True:
    if num < b :
        answer.append(num)
        break
    
    answer.append(num % b)
    num //= b


# 출력 
for i in answer[::-1]:
    print(i, end = "")

