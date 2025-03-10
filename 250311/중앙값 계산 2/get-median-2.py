n = int(input())
arr = list(map(int, input().split()))

num_list=[]

for i in range(n):
    num_list.append(arr[i])
    if (i+1) % 2 != 0:
        num_list.sort()
        print(num_list[len(num_list)//2], end = " ")


