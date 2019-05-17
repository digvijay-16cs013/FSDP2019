# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:45:59 2019

@author: Administrator
"""
import random

def get_position():
    return random.randint(0, 3), random.randint(0, 3)

def show_matrix(maze):
    for line in maze:
        for room in line:
            print(room, end = ' ')
        print()

player_x, player_y = get_position()

monster_x, monster_y = get_position()

while monster_x == player_x and monster_y == player_y:
    monster_x, monster_y = get_position()
    
exit_x, exit_y = get_position()

while (exit_x == player_x and exit_y == player_y) or (exit_x == monster_x and exit_y == monster_y):
    exit_x, exit_y = get_position()
    
print('Welcome to Dungeon Game...')

maze = [['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']]

maze[player_x][player_y] = '!'

print('\n! - Your player\n\n')

show_matrix(maze)

while True:
    
    maze[player_x][player_y] = '?'    
    choice = input('Enter choice :-\npress : "r" for right\npress : "l" for left\npress : "t" for top\npress : "d" for down\n\n')
    
    if choice.lower() == 'r':
        if player_y + 1 <= 3:
            player_y += 1
        else:
            print('\nyou can\'t go out of the box\n')
    
    elif choice.lower() == 'l':
        if player_y - 1 >= 0:
            player_y -= 1
        else:
            print('\nyou can\'t go out of the box...\n')
        
    elif choice.lower() == 't':
        if player_x - 1 >= 0:
            player_x -= 1
        else:
            print('\nyou can\'t go out of the box...\n')
        
    elif choice.lower() == 'd':
        if player_x + 1 <= 3:
            player_x += 1
        else:
            print('\nyou can\'t go out of the box...\n')
            
    else:
        print('\nEnter right choice\n')
        

    if player_x == monster_x and player_y == monster_y:
        maze[player_x][player_y] = ':('
        show_matrix(maze)
        print('\nPlayer lose...\nGame Over...')
        break
        
    elif player_x == exit_x and player_y == exit_y:
        maze[player_x][player_y] = ':)'
        show_matrix(maze)
        print('\nHurrah! Player wins...')
        break
    
    else:
        maze[player_x][player_y] = '!'
        show_matrix(maze)
        