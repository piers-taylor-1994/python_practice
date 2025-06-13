import random
import hangman_words
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
lives = 6
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

guessed_letters = []
game_over = False
display = placeholder

while not game_over:
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print(f"You have already guessed {guess}")
    else:
        guessed_letters.append(guess)
        displayList = list(display)

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                displayList[i] = guess

        display = "".join(displayList)

        print(display)

        # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
        #  If lives goes down to 0 then the game should stop and it should print "You lose."

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
                game_over = True
                print(f"The word was {chosen_word}")
                print(f"***********************YOU LOSE**********************")

        elif "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        # TODO-3: - print the ASCII art from 'stages'
        #  that corresponds to the current number of 'lives' the user has remaining.
        print(hangman_art.stages[lives])