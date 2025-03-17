# #배열을 돌면서 , B를 찾고, 해당 B와 마지막 행,열의 차이만큼 곱하기 

# r,c = map(int, input().split())

# arr = [list(map(str, input().split()))for i in range(r)]

# cnt = 0 

# for i in range(1, r - 1):
#     for j in range(1, c - 1):
#         for k in range(i+1, r - 1):
#             for l in range(j+1, c-1):
#                 if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[r-1][c-1]:
#                     # print(i,j)
#                     # print(k,l)
#                     # print("---")
#                     cnt += 1
    
# print(cnt)

#배열을 돌면서 , B를 찾고, 해당 B와 마지막 행,열의 차이만큼 곱하기 

#배열을 돌면서 , B를 찾고, 해당 B와 마지막 행,열의 차이만큼 곱하기 

r,c = map(int, input().split())

arr = [list(map(str, input().split()))for i in range(r)]

cnt = 0 

for x in range(1, r - 1):
    for y in range(1, c - 1):
        if arr[x][y] == "B":
            cnt += (r - x - 2) * (c - y - 2)
    

if arr[0][0] == arr[r-1][c-1]:
    print("0")
else: 
    print(cnt)