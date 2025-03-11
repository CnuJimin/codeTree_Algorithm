n = int(input())

class Pos:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num


array = []

for i in range(n):
    x,y = map(int, input().split())
    array.append(Pos(x, y, i+1))

array.sort(key = lambda x : abs(x.x) + abs(x.y))


for pos in array:
    print(pos.num)
    