n = list(input())

def change(num): #2진수를 리스트로 받아서 10진수 정수로 리턴 

    arr = list(map(int, num))
    result = 0 

    for i in range(len(arr)):
        result = result * 2 + arr[i]
    
    return result

ans = 0 



for i in range(len(n)):
    
    backup = n[:]

    if backup[i] == "0":
        backup[i] = "1"
    else:
        backup[i] = "0"

    # print(*backup)
    # print(change(backup))
    ans = max(ans, change(backup))

print(ans)