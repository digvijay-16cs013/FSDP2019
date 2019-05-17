# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:31:42 2019

@author: Administrator
"""

# Importing randint method from random
from random import randint

# Outer loop to ask user to play again
while True:
    # Random number for computer
    secret_num = randint(1, 10)
    
    # Chance variable to give user another chance
    chance = 1
    
    # Inner loop to give user maximum 6 chance in case he guesses wrong
    while chance <= 6:
        
        # To identify the exception i.e. non integer submission by user 
        try:
            
            # To take user input from 1 to 10
            guessed_num = int(input('Enter an integer from 1 to 10 : '))
        
            # Condition to check whether user guessed right
            if secret_num == guessed_num:
                print('Player wins and Computer lose')
                
                # Jumping out of the loop if he guesses right
                break
            
            # If user doesn't guess right
            else:
                print('Player lose and Computer wins')
                
                # Printing the secret number and guessed number
                print('The secret number : {} \nThe guessed number : {}'.format(secret_num, guessed_num))
                
                # Printing too high if user guesses too high number from secret number
                if guessed_num - secret_num >= 6:
                    print('Your guess is too high')
                    
                # Printing too low if user guesses too low number from secret number
                elif guessed_num - secret_num <= -6:
                    print('Your guess is too low')
                
                # Printing remaining chances out of 6
                print('You have', (6 - chance), 'attempts left')
                
                # Increment chance
                chance += 1
                
        # Handling exception (non integer submission by user)
        except ValueError:
            # Making the user aware
            print('ValueError : Enter only integer values')
        
    # Asking to play again from user
    choice = input('Do you want to play again \nPress "y" for Yes and Any other key for No : ')
    
    # Checking if user enters 'Y' or 'y'
    if choice.lower() != 'y':
        break
    
# Game ended
print('Game Over...')       
        
