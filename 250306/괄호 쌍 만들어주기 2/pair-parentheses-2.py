arr = input()
L = len(arr)

cnt = 0

#각 i 번째 괄호에 대해서, 그 괄호가 (일 때 그 그 다음 괄호도 (이면 
for i in range(L - 1):
    if arr[i : i+2] == "((":
        #그 다음 괄호 j부터 (j는 i+1 보다 커야함) 연속된 ))를 찾음 
        for j in range(i + 2, L - 1):
            if arr[j:j+2] == "))":
                cnt += 1

print(cnt)