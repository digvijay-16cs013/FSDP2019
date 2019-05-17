# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""
# to import random module
import random

# list of fruits
fruits = ['Apple', 'Mango', 'Orange', 'Banana', 'Guava']

# to choose random fruit from fruits list
secret_word = random.choice(fruits)

# to convert the string in list of characters
secret_word = list(secret_word)

# to generate spaces which is equals to numbers of characters in the secret_word
fruit = list(len(secret_word) * '_')

# Max tries for user
chance = 10

# to chance if chances excceed
while chance > 0:
    # get the first letter entered by user
    guessed_letter = input('Enter letter of fruit => ')[0]
    
    # get individual letter and index from secret word
    for index, letter in enumerate(secret_word):
        
        # check if letter entered by user is a right guess
        if letter == guessed_letter:
            
            # update the space in fruit list by letter
            fruit[index] = letter
    
    # print word after guessing the letter        
    for letter in fruit:
        print(letter, end = ' ')
        
    # to check if user has found the correct word
    if fruit == secret_word:
        
        # player wins
        print('\n\nPlayer wins and Computer lose')
        
        # get out of the loop
        break
    
    # reducing chances by 1.
    chance = chance - 1

    # show the no of tries left
    print('\n\nYou have', chance, 'tries left')
            
# after all the chances finished check if user could not guess the correct word
if fruit != secret_word:
    
    # computer wins
    print('\nPlayer lose and Computer wins')
    
"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

import random

# to show guessed_word
def show_guessed_word(fruit):
    
    # getting individual character from fr list
    for letter in fruit:
        print(letter, end = ' ')

def Hangman():
    # list of fruits
    fruits = ['Apple', 'Mango', 'Orange', 'Banana', 'Guava']
    
    # to choose random fruit from fruits list
    secret_word = random.choice(fruits)
    
    # to convert the string in list of characters
    secret_word = list(secret_word)
    
    # to generate spaces which is equals to numbers of characters in the secret_word
    fruit = list(len(secret_word) * '_')
    
    # Max tries for user
    chance = 10
    
    # to chance if chances excceed
    while chance > 0:
        # get the first letter entered by user
        guessed_letter = input('Enter letter of fruit => ')[0]
        
        # get individual letter and index from secret word
        for index, letter in enumerate(secret_word):
            
            # check if letter entered by user is a right guess
            if letter == guessed_letter:
                
                # update the space in fruit list by letter
                fruit[index] = letter
        
        # print word after guessing the letter        
        show_guessed_word(fruit)
            
        # to check if user has found the correct word
        if fruit == secret_word:
            
            # player wins
            print('\n\nPlayer wins and Computer lose')
            
            # get out of the loop
            break
        
        # reducing chances by 1.
        chance = chance - 1
    
        # show the no of tries left
        print('\n\nYou have', chance, 'tries left')
                
    # after all the chances finished check if user could not guess the correct word
    if fruit != secret_word:
        
        # computer wins
        print('\nPlayer lose and Computer wins')
        
Hangman()

"""
Challenge 3
Read the words from a file

"""

"""
Challenge 4
    Get the list of Internet after web scrapping
"""
