n = int(input())

class Student:
    def __init__(self, tall, weight, num):
        self.tall = tall
        self.weight = weight
        self.num = num

students = []

for i in range(n):
    tall, weight = map(int, input().split())
    students.append(Student(tall, weight, i+1))


students.sort(key = lambda x : (x.tall, -x.weight))

for student in students:
    print(student.tall, student.weight, student.num)