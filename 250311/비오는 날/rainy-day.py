n = int(input())

class Weather:
    def __init__ (self, time, date, weather):
        self.time = time
        self.date = date
        self.weather = weather

weahters = []

for _ in range(n):
    time, date, weather = map(str, input().split())
    weahters.append(Weather(time, date, weather))

rainny = []

for i in range(n):
    if weahters[i].weather == "Rain":
        rainny.append(weahters[i])

fast_index = 0 

for i in range(1, len(rainny)):
    if rainny[fast_index].time > rainny[i].time:
        fast_index = i

print(rainny[fast_index].time, rainny[fast_index].date, rainny[fast_index].weather)