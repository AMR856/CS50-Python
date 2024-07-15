#!/usr/bin/python3
INPUT_MSG = 'Input: '
OUTPUT_MSG = 'Output: '
VOWELS = ['a', 'e', 'i', 'o', 'u']
# NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# PUNCTUATION = ['!', '"', '#', '$', '%', '&', "'",
#             '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
#             '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_',
#             '`', '{', '|', '}', '~']

def main():
    user_input = input(INPUT_MSG)
    print(shorten(user_input))


def shorten(word):
    output_string = ''
    for i in range(len(word)):
        if word[i].lower() not in VOWELS:
            output_string += word[i]
    return output_string

if __name__ == "__main__":
    main()
