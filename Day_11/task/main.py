from operator import indexOf

import art
import random

def score_total(user):
    return sum(data[user]["Cards"])

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

data = {
    "Me": {
        "Cards": [],
        "Score": 0,
        "Money": 100.0,
        "Bet": 0.0,
    },
    "Computer": {
        "Cards": [],
        "Score": 0
    }
}

def calculate_score(user):
    total = sum(data[user]["Cards"])
    data[user]["Score"] = total
    if total > 21:
        if 11 in data[user]["Cards"]:
            data[user]["Cards"][indexOf(data[user]["Cards"],11)] = 1
            calculate_score(user)

def deal_cards(user):
    card = random.choice(cards)
    data[user]["Cards"].append(card)
    calculate_score(user)

def confirm_winner():
    user_score = data["Me"]["Score"]
    comp_score = data["Computer"]["Score"]

    if user_score == comp_score:
        print("You draw")
    elif user_score > 21 or (comp_score <= 21 and user_score < comp_score):
        print("You lose")
        data["Me"]["Money"] -= data["Me"]["Bet"]
        if data["Me"]["Money"] < 0.0:
            data["Me"]["Money"] = 0.0
    else:
        print("You win")
        data["Me"]["Money"] += data["Me"]["Bet"]
    print(f"Balance now £{'{0:.2f}'.format(data["Me"]["Money"])}")

def reset_cards():
    data["Me"]["Cards"] = []
    data["Me"]["Score"] = 0
    data["Computer"]["Cards"] = []
    data["Computer"]["Score"] = 0

def blackjack():
    print(art.logo)
    for i in range (1):
        deal_cards("Me")
    deal_cards("Computer")
    while data["Me"]["Score"] <= 21:
        print(f"Your cards: {data["Me"]["Cards"]}, current score: {data["Me"]["Score"]}")
        print(f"Computer's first card: {data["Computer"]["Cards"][0]}")
        continue_play = input("Draw another card? 'y' or 'n': ")
        if continue_play == "y":
            deal_cards("Me")
        else:
            break
    if data["Me"]["Score"] <= 21:
        deal_cards("Computer")
        if data["Computer"]["Score"] < 17:
            deal_cards("Computer")
    print(f"Your final hand: {data["Me"]["Cards"]}, final score: {data["Me"]["Score"]}")
    print(f"Computer's final hand: {data["Computer"]["Cards"]}, final score: {data["Computer"]["Score"]}")
    confirm_winner()
    if data["Me"]["Money"] <= 0.0:
        print("You have run out of money. Game over.")
    else:
        play_game(False)

def play_game(first_round):
    play = input("Do you want to play a game of black? Type 'y' or 'n': ")
    if play == "y":
        print(f"You current have £{'{0:.2f}'.format(data["Me"]["Money"])}")
        data["Me"]["Bet"] = float(input("How much do you want to bet? £"))
        if not first_round:
            reset_cards()
            print("\n" * 50)
        blackjack()
play_game(True)