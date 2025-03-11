code, color, time = map(str, input().split())

class UnLock:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

solve = UnLock(code, color, time)

print(f"code : {solve.code}\ncolor : {solve.color} \nsecond : {solve.time}")