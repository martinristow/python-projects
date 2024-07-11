# Input a list of student scores
student_scores = input("Input a list of student scores:\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for student in student_scores:
    if highest_score < student:
        highest_score = student

print(f"The highest score in the class is: {highest_score}")


