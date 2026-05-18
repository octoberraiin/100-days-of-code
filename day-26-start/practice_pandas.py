# Looping through dictionaries

student_dict = {
    "student": ["Angela", "Whiskey", "Pip"],
    "score": [34, 36, 25]
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_df = pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)