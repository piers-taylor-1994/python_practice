#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

contents = ""
names = []

with open("Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:
    contents = start_letter.read()

with open("Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as names_letter:
    for n in names_letter.read().split("\n"):
        names.append(n)

for name in names:
    with open(f"Day 24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_letter:
        new_content = contents.replace("[name]", name).replace("Angela", "Piers")
        output_letter.write(new_content)