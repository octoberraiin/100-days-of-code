numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)


name = "Megha"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# List Comprehension Examples
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)


import random

# Dictionary Comprehension Examples
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


