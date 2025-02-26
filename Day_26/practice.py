import random
numbers = 1, 2, 3
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_list2 = [r*2 for r in range(1,5)]
print(new_list2)

names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

students_scores = {student:random.randint(1, 99) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)