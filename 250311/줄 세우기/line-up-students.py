n = int(input())

students = []

class Student:
    def __init__(self, tall, weight, number):
        self.tall = tall
        self.weight = weight
        self.number = number

for i in range(n):
    tall, weight = map(int, input().split())
    students.append(Student(tall, weight, i + 1))

students.sort(key = lambda x : (-x.tall, -x.weight, x.number))

for student in students:
    print(student.tall, student.weight, student.number)