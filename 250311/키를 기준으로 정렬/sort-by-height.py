n = int(input())

class Person:
    def __init__ (self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

people = []

for _ in range(n):
    name, tall, weight = map(str, input().split())
    people.append(Person(name, tall, weight))


people.sort(key = lambda x : x.tall)

for person in people:
    print(person.name, person.tall, person.weight)