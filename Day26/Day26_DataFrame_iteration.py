student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)

# for (key, value) in student_dataframe.items():
#     print(value)

for (index, row) in student_dataframe.iterrows():
    print(row.student)