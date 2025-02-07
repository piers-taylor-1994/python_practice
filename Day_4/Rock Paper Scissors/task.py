import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, len(choices) - 1)

if choice <= 2:
    print(choices[choice])

print(f"Computer chose:\n{choices[computer_choice]}")
#other way of writing^ random.choice(choices)

if choice >= 3:
    print("Invalid number entered, you lose")
elif choice == computer_choice:
    print("It's a draw")
else:
    if choice == 0 and computer_choice == 2 or choice == 1 and computer_choice == 0 or choice == 2 and computer_choice == 1:
        print("You win")
    else:
        print("You lose")