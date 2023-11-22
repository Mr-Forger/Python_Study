import random

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

new_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(new_students)