import pandas

student_dict = {
    "student": ["Martin", "Filip", "Natasha", "Tane"],
    "score": [35, 48, 84, 67]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row.student)
    if row.student == "Martin":
        print(row.score)
