#Step 5

import os
import random
import hangman_words
import hangman_art

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

used_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')
    print(hangman_art.logo)
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in used_letters:
        print(f"You've already guessed {guess}\n")
    else:
        used_letters += guess

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    
        #Check if user is wrong.
        if guess not in chosen_word:
            #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
            lives -= 1
    
        #Join all the elements in the list and turn it into a String.
        # print(hangman_art.stages[lives])
        # print(f"{' '.join(display)}")
    
        if "_" not in display or lives == 0:
            end_of_game = True
            
    
        #Check if user has got all letters.
        # if "_" not in display:
        #     end_of_game = True
            

    
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}\n")
    print(f"LETTERS ALREADY GUESSED {used_letters}\n")

if lives == 0:
    os.system('clear')
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}\n")
    print(f"The correct word was {chosen_word}.\n")
    print(hangman_art.lose)

if "_" not in display:
    os.system('clear')
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}\n")
    print(hangman_art.win)
    