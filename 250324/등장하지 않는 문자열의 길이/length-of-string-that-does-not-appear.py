#n개의 문자에서 앞에서부터 i개의 문자열을 선택하고, 해당 문자열이 또 등장하는지 확인, 등장하지 않는다면 그 길이가 최소 

n = int(input())

word = list(input())

sub = [] 

for i in range(n):
    for k in range(1, n):
        for j in range(i+k+1, n):
            if word[i:i+k+1] == word[j:j+k+1]:
                # print(*word[i:i+k+1])
                sub.append(k)

result = max(sub) + 2 

print(result)