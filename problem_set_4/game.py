#!/usr/bin/python3
from multiprocessing import Value
import random
INPUT_MSG_1 = 'Level: '
INPUT_MSG_2 = 'Guess: '
level_input = ''

while True:
    try:
        level_input = int(input(INPUT_MSG_1))
        if level_input >= 1 and level_input <= 100:
            break
        continue
    except ValueError:
        continue

the_random_number = random.randint(1, level_input)
while True:
    try:
        user_guess = int(input(INPUT_MSG_2))
        if user_guess == the_random_number:
            print("Just right!")
            break
        elif user_guess > the_random_number:
            print('Too large!')
            continue
        elif user_guess < the_random_number:
            print('Too small!')
            continue
        elif user_guess <= 0:
            continue
    except ValueError:
        continue