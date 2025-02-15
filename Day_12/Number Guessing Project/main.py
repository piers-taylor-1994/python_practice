import art
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100
HARD_CHANCES = 7
EASY_CHANCES = 15

def create_number():
    return random.randint(LOWER_LIMIT, UPPER_LIMIT)

def set_chances(difficulty):
    if difficulty == "easy":
        return EASY_CHANCES
    else:
        return HARD_CHANCES

def decrement_chances(c):
    return c - 1

def process_chances(g, n, c):
    if g < n:
        print("Too low.")
    else:
        print("Too high.")
    if c > 1:
        print("Guess again.")
    return decrement_chances(c)


def number_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWER_LIMIT} and {UPPER_LIMIT}.")
    number = create_number()
    #print(number)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    chances = set_chances(difficulty)
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Well done, you guessed the number correctly")
            return
        else:
            chances = process_chances(guess, number, chances)
    play_again = input("You ran out of guesses. Type 'r' to start again: ")
    if play_again == "r":
        print("\n" * 30)
        number_game()
number_game()