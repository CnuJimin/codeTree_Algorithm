n = int(input())

class Person:
    def __init__(self, name, street, city):
        self.name = name
        self.street = street
        self.city = city

people = []

for _ in range(n):
    name, street, city = map(str, input().split())

    people.append(Person(name, street, city))

max_value = 0 

for i in range(1, n):
    if people[max_value].name < people[i].name:
        max_value = i

print(f"name {people[max_value].name} \naddr {people[max_value].street} \ncity {people[max_value].city}")