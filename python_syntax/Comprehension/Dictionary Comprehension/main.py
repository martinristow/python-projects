import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_score = {student: random.randint(0, 100) for student in names}
print(students_score)

# pass_students = {}
# for student in students_score:
#     if students_score[student] >= 50:
#         pass_students.update({student: students_score[student]})
# print(pass_students)
# 5 lines code converted to 2 lines code
# passed_students = {new_key: new_value for (key, value) in dictionary.items() if test}
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)
