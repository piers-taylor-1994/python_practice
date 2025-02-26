import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

def generate_phonetic():
    with open("Day_26/NATO-alphabet-start/nato_phonetic_alphabet.csv") as file:
        csv = pandas.read_csv(file)
    alphabet_dict = {row.letter:row.code for (index, row) in csv.iterrows()}
    word = input("Enter a word: ").upper()
    try:
        output_word = [alphabet_dict[letter] for letter in word]
        
    except KeyError:
        print(f"Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_word)
generate_phonetic()