#!/usr/bin/python3
INPUT_MSG = 'Fraction: '
while True:
    try:
        user_input = input(INPUT_MSG ).split('/')
        x, y = user_input[0], user_input[1]
        division_result = round(int(x) / int(y), 2)
        print(division_result)
        if (division_result > 1):
            continue
        percentage = division_result * 100
        if percentage >= 99:
            print('F')
        elif percentage <= 1:
            print('E')
        else:
            print(f'{int(percentage)}%')
        break
    except (ValueError, ZeroDivisionError, IndexError):
        continue
