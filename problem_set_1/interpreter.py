#!/usr/bin/python3
INPUT_MSG = 'Expression: '
ALLOWED_OPERATOINS = ['+', '-', '*', '/']
x, y, z = input(INPUT_MSG).split(" ")
if y in ALLOWED_OPERATOINS:
    if (y == '+'):
        print(f'{float(x) + float(z)}')
    elif (y == '-'):
        print(f'{float(x) - float(z)}')
    elif (y == '*'):
        print(f'{float(x) * float(z)}')
    else:
        print(f'{float(x) / float(z)}')
else:
    print("Incorrent operator")
