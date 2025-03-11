#키 오름차순, 동일할 경우 몸무게 내림차순 

n = int(input())

class Person:
    def __init__ (self, name, tall, weight):
        self.name = name 
        self.tall = tall
        self.weight = weight

people = []

for _ in range(n):
    name, tall, weight = map(str, input().split())
    people.append(Person(name, int(tall), int(weight)))

people.sort(key = lambda x : (x.tall, -x.weight))

for person in people:
    print(person.name, person.tall, person.weight)