n = int(input())

students = []

class Student:
    def __init__(self, name,a,b,c):
        self.name = name 
        self.a = a
        self.b = b
        self.c = c

for _ in range(n):
    name, a, b, c = map(str, input().split())
    students.append(Student(name, int(a), int(b), int(c)))


students.sort(key = lambda x : x.a + x.b + x.c)

for student in students:
    print(student.name, student.a, student.b, student.c)