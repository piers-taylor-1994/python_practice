import math
import random
# ---------------------------- Variables ------------------------------- #
text = "Hello"
number = 5
decimal = 0.5
float = 0.5
correct = True

# ---------------------------- Dynamic typing ------------------------------- #
text_2 = "Hello"
if text_2 == "Hello":
    text_2 = 5
print(text_2)

# ---------------------------- Constants ------------------------------- #
CONSTANT_1 = "Test"
CONSTANT_2 = 120

# ---------------------------- String manipulation ------------------------------- #
#Split a string into a list given a specific seperator
text_3 = "H-e-l-l-o"
text_3_list = text_3.split("-")
print(text_3_list)

#Split a normal string into a list
text_4 = "hello"
text_4_list = list(text_4)
print(text_4_list)

#Remove trailing whitespace
text_5 = "H ell o   "
text_5_stripped = text_5.strip()
print(text_5_stripped)

#Stitch a list of strings together
text_list = ["He", "ll", "o", "!"]
text_6_join = "".join(text_list)
print(text_6_join)

#Replace characters in a string
text_6 = "Hello"
text_6_new = text_6.replace("e", "!")
print(text_6_new)

# ---------------------------- Int manipulation ------------------------------- #
outcome = 5 / 6
print(outcome)

outcome_2 = 5 // 6
print(outcome_2)

outcome_3 = 5 * 2
print(outcome_3)

outcome_4 = 5 ** 2
print(outcome_4)

print(round(outcome, 2))

print(max([1,2,3,10,5,6,7]))

# ---------------------------- Dictionaries ------------------------------- #
dict = {
    "name": "Piers",
    "age": 30
}
# ---------------------------- Functions ------------------------------- #
# ---------------------------- For loops ------------------------------- #
output = ""
for letter in "hello":
    output += f"{letter}!"
print(output)

numbers = ["1", "2", "3"]
list_2 = [letter for letter in "test123" if letter in numbers]
print(list_2)

dict_1 = {l:random.randint(0, 10) for l in "test321"}
print(dict_1)

dict_2 = {f"new {letter}":number + 100 for (letter, number) in dict_1.items()}
print(dict_2)