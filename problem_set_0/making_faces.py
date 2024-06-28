#!/usr/bin/python3
INPUT_MSG = 'Please, input your message: \n'

def convert(input_string: str) -> str:
    return input_string.replace(':)', '🙂').replace(':(', '🙁')


def main():
    the_user_message = input(INPUT_MSG)
    print(convert(the_user_message))

main()