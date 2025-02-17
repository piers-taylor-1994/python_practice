#import logo, data, random
import art
import game_data
import random

b = random.choice(game_data.data)
score = 0

def format_data(d_entry, letter):
    return f"Compare {letter}: {d_entry["name"]}, a {d_entry["description"]}, from {d_entry["country"]}"

def check_answer(choice1, choice2, answ):
    if choice1["follower_count"] > choice2["follower_count"]:
        return answ == "a"
    else:
        return answ == "b"

# Not used
def switch(choice1, choice2):
    (choice1, choice2) = (choice2, choice1)
    return choice1, choice2

def game():
    global score
    global b

    a = b
    while b == a:
        b = random.choice(game_data.data)

    print(art.logo)

    if score > 0:
        print(f"You're right! Current score: {score}")

    print(format_data(a, "A"))
    print(art.vs)
    print(format_data(b, "B"))

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if check_answer(a, b, answer):
        score += 1
        print("\n" * 20)
        game()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
game()