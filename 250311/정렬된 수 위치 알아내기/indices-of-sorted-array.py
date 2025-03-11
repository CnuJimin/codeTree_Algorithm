n = int(input())
arr = []
nums = list(map(int, input().split()))


class Num :
    def __init__ (self, num, order):
        self.num = num
        self.order = order

for i in range(n):
    arr.append(Num(nums[i], i))

arr.sort(key = lambda x : x.num)


number = []
num_to_rank = [0] * n

for i in arr:
    number.append(i.order)

for rank, num in enumerate(number, start = 1):
    num_to_rank[num] = rank

print(*num_to_rank)