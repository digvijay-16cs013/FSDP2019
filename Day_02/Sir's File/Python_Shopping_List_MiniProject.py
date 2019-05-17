# Shopping List App 

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""


#   Make a list to hold onto our items.
shopping_list = []

# Print out instructions on how to use the app
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    
    # add new items to our list
    shopping_list.append(new_item)

#  print out the list
print("Here’s your list")
for item in shopping_list:
    print ( item )



"""
Challenge 2
    If I type SHOW, 
    I should be able to see what is currently in the list

    If I type HELP, 
    I should be able to see all the help for these special commands

Hint 2
    Step 1: Have a HELP command
    Step 2: Have a SHOW command
    Step 3: Add a function for adding into the list 
    Step 4: Cleanup the code in general
    
"""
shopping_list = []

print ('What would you like to pick up from store ?')

# Print out instructions on how to use the app
def instructions():
    print('\nHere are some instructions :-')
    print ('Enter "DONE" to stop adding items.')
    print('Enter "SHOW" to display current contents in the list.')
    print('Enter "HELP" to display instructions.')

def add_items(shop_list):
    while True:
        # ask for new items
        new_item = input("> ")
    
        # to stop adding items in the list
        if new_item == 'DONE':
            break
        
        # to show current items in the list
        elif new_item == 'SHOW':
            print('Here is your list :-')
            for item in shop_list:
                print('>', item)
        
        # to display instructions
        elif new_item == 'HELP':
            instructions()
            
        # add new items to our list
        else:
            shop_list.append(new_item)

#  print out the list
instructions()
add_items(shopping_list)
print("\nHere’s your list")
for item in shopping_list:
    print ( item )

"""

Challenge 3
    User can enter SHOW or Show or show, 
    similar for DONE and HELP, but the program should do the required job

    Show the item in the list serially starting from 1

    Let us accept items using a comma separated string
        
    Also there should be a functionality to add an item at a specific index

    There should be a functionality to remove items from the list at a specific index using REMOVE
    
    Do all the exception handling for all the extreme use cases 
"""

shopping_list = []

print ('What would you like to pick up from store ?')

# Print out instructions on how to use the app
def instructions():
    print('\nHere are some instructions :-')
    print ('Enter "DONE" to stop adding items.')
    print('Enter "SHOW" to display current contents in the list.')
    print('Enter "HELP" to display instructions.')
    print('Enter "ADD" to add items to specific location.')
    print('Enter "REMOVE" to remove items from a specific location.')
    print('Enter item name to add item at the end of list.\n')

def add_items(shop_list):
    
    while True:
        
        # ask for new items
        new_item = input("> ")
        # to stop adding items in the list
        if new_item.upper() == 'DONE':
            break
        
        # to show current items in the list
        elif new_item.upper() == 'SHOW':
            print('Here is your list :-')
            for index in range(len(shop_list)):
                print('Item number :', index + 1, 'Item Name :', shop_list[index])
            
        
        # to display instructions
        elif new_item.upper() == 'HELP':
            instructions()
            
            
        # to add items to a specific location    
        elif new_item.upper() == 'ADD':
            
            # to get postition of item
            idx = int(input('Enter position : '))
            
            # to check if position is correct
            if idx not in range(1, len(shop_list) + 1):
                print('Enter correct position...')
                continue
            
            # to get item value
            value = input('Enter item name : ')
            
            # to insert item at specified location
            shop_list.insert(idx - 1, value)
            
            
        # to remove item from a specific location
        elif new_item.upper() == 'REMOVE':
            
            # to get postition of item
            idx = int(input('Enter position : '))
            
            # to check if position is correct
            if idx not in range(1, len(shop_list) + 1):
                print('Enter correct position...')
                continue
    
            # to remove item from specified location
            print('item', shop_list.pop(idx - 1), 'removed')
        
        # to add items at the end of list
        else:
            shop_list.append(new_item)    
            
        

# take items from user
shopping_list = input('Enter comma separated items in the list => ').split(',')

#  print out the instructions to add items
instructions()

# to item in the existing list
add_items(shopping_list)


print("\nHere’s your list")
for item in shopping_list:
    print ( item )

# challenge 5:-
with open('shopping_list.txt', 'w') as fp:
    
    for word in shopping_list:
        fp.write(word + '\n')

"""
Challenge 4   
    Do all the exception handling for all the extreme use cases 
"""

"""
Challenge 5   
    Store the shopping list in a file. 
"""


