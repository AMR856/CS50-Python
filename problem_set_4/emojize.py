#!/usr/bin/python3
import emoji
INPUT_MSG = 'Input: '
OUTPUT_MSG = 'OUTPUT: '
user_input = input(INPUT_MSG)
emojized_input = emoji.emojize(user_input, language='alias')
print(f'{OUTPUT_MSG}{emojized_input}')
