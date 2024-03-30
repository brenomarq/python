# Hangman Game Project
import random
import hangman_art
import hangman_words
import os

chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

display = ["_" for _ in range(len(chosen_word))]
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("clear")

    if guess in display:
        print(f"You've already guessed this letter: {guess}")

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if guess == chosen_word[index]:
                display[index] = guess
    else:
        print(f"The letter {guess} is not in the word, you lose a life.")
        lives -= 1

    complete_word = "".join(display)

    print(complete_word)
    print(hangman_art.stages[lives])

    if lives == 0:
        print("You lose!")
        end_of_game = True

    complete_word = "".join(display)
    if complete_word == chosen_word:
        print(f"The secret word was {chosen_word}")
        print("You win!")
        end_of_game = True
