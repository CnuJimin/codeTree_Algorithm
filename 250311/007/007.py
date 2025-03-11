code, place, time = map(str, input().split())

class Mission :
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

mission = Mission(code, place, time)

print("secret code : " + mission.code)
print("meeting point : " + mission.place)
print("time : " + mission.time)