class agent:
    def __init__ (self, codeName, score):
        self.codeName = codeName
        self.score = score

agents = []

for i in range(5):
    codeName, score = tuple(map(str, input().split()))
    agents.append(agent(codeName, int(score)))



min_index = 0 

for i in range(1,5):
    if agents[min_index].score > agents[i].score:
        min_index = i

print(agents[min_index].codeName, agents[min_index].score)
