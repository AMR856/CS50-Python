#!/usr/bin/python3
INPUT_MSG = 'Greeting: '
greeting = input(INPUT_MSG).strip().lower().split()
if greeting[0].strip(',').strip('-') == 'hello':
    print('$0')
elif greeting[0][0] == 'h':
    print('$20')
else:
    print('$100')
