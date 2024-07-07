#!/usr/bin/python3
import sys
from pyfiglet import Figlet
import random
# print(sys.argv) first => filename

def program_failure():
    print('Invalid usage')
    sys.exit(1)

INPUT_MSG = 'Input: '
OUTPUT_MSG = 'Output: '
figlet = Figlet()
font_list = figlet.getFonts()
font_name = ''

if len(sys.argv) == 1:
    font_name = random.choice(font_list)
elif len(sys.argv)  <= 3:
    try:
        font_notation = sys.argv[1]
        font_name = sys.argv[2]
        if font_notation not in ['-f', '--font'] or font_name not in font_list:
            raise ValueError
    except (IndexError, ValueError):
        program_failure()

user_input = input(INPUT_MSG)
figlet.setFont(font=font_name)
print(OUTPUT_MSG)
print(figlet.renderText(user_input))
