# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
number_of_students = 0
average_height = 0

for student_height in student_heights:
    number_of_students += 1

for total in student_heights:
    total_height += total

average_height = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")
