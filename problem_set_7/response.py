#!/usr/bin/python3
import validators
INPUT_MSG = 'Email: '

def main():
    user_input = input(INPUT_MSG).strip()
    if validators.email(user_input): 
        print('VALID')
    else:
        print('INVALID')


if __name__ == '__main__':
    main()
