#!/usr/bin/python3
INPUT_MSG = 'Input: '
OUTPUT_MSG = 'Output: '
VOWELS = ['a', 'e', 'i', 'o', 'u']
user_input = input(INPUT_MSG)
output_string = ''
for i in range(len(user_input)):
    if user_input[i].lower() not in VOWELS:
        output_string += user_input[i]
print(f'{OUTPUT_MSG}{output_string}')
