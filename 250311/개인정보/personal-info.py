class Person:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

people = []

for i in range(5):
    name, tall, weight = map(str, input().split())
    people.append(Person(name, int(tall), float(weight)))


#이름 순으로 정렬 
people.sort(key = lambda x : x.name)

print("name")
for person in people:
    print(f"{person.name} {person. tall} {person.weight:.1f}")

print()
#이름 순으로 정렬 
people.sort(key = lambda x : -x.tall)

print("height")
for person in people:
    print(f"{person.name} {person. tall} {person.weight:.1f}")
