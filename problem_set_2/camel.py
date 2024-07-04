#!/usr/bin/python3
INPUT_MSG = 'camelCase: '
OUTPUT_MSG = 'snake_case: '
user_input = list(input(INPUT_MSG))
for i in range(len(user_input)):
    if user_input[i].isupper():
        user_input[i] = user_input[i].lower()
        user_input.insert(i, '_')
output = ''
print(f'{OUTPUT_MSG}{output.join(user_input)}')
