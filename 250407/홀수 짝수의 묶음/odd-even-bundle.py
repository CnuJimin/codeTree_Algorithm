#앞에서부터 짝수가 될 때 까지 구함, 그리고 홀수를 구함, 짝수를 구함.. 
#음 근데 그 다음 수가 남아 있는데 짝,홀을 구할 수 없을 때가 문제임 
# 11 2 17 / 13/ 1 15/ 3 
# 2 
# 1 3 11 13 15 17 -> 6개 짝수개 
# 2 / 1 / 3 11/ 13 / 15 17

# 짝수, 홀수개 각각 존재하는 만큼 그냥 가능 
# 근데 짝수 개수가 더 많으면 홀수개 기준으로 개수를 세야 함 
# 홀수개가 더 많으면, 짝수, 홀수 개수에서 -> 2, 1, 해서 0까지 

#1 3 3 5 7 9 11 -> 홀수만 7개 -> 2  1  2 1 
# 13/ 3 / 57911

# 2, 4, 6
# 1 ,3 
# 2, 1, 4, 3


# 1. 짝수만 있을 경우 -> 1개 
# 2. 홀수만 있을 경우 -> 2, 1, 번갈아가면서 빼다가 0이 되면 딱 떨어짐 그럼 개수에서 -1 , 1이 남게 되면 멈추고 -1 
# 3. 짝수가 더 많을 경우 -> 짝,홀 동일하게 남은 개수만큰 가능하고, + 1 
# 4. 홀수가 더 많을 경우 -> 짝, 홀 동일하게 남은 개수만큼 하고, 남은 홀수 개수에서 2,1,2.1 빼면서 홀수만 있는 경우랑 동일하게 가면 됨 

n = int(input())

arr = list(map(int, input().split()))

odd = [] 
even = [] 

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

cnt = [2,1]

# 짝수만 존재할 경우 
if len(odd) == 0 :
    ans = 1 
# 홀수만 존재할 경우 
elif len(even) == 0 :
    odd_cnt = len(odd)
    ans = 0
    i = 0 
    while True:
        if odd_cnt == 1:
            ans -= 1
            break
        elif odd_cnt == 0 :
            break
        odd_cnt -= cnt[i%2]
        ans += 1
        i += 1
    # ans -= 1

elif len(even) == len(odd):
    ans = 2 * len(odd)

elif len(even) > len(odd):
    ans = len(odd) * 2 + 1

elif len(even) < len(odd):
    ans = len(even) * 2 
    odd_cnt = len(odd) - len(even)
    i = 0 
    while True:
        if odd_cnt == 1:
            ans -= 1
            break
        elif odd_cnt == 0 :
            break
        odd_cnt -= cnt[i%2]
        ans += 1
        i += 1

print(ans)
