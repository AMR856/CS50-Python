#!/usr/bin/python3

punctuation_list = set(['.', ' ', '!', '"', '#', '$', '%', '&',
                    "'", '(', ')', '*', '+', ',', '-', '.',
                    '/', ':', ';','<', '=', '>', '?','@',
                    '[', '\\', ']','^', '_', '`', '{', '|',
                    '}', '~'])

alphabet = list("abcdefghijklmnopqrstuvwxyz")
numbers = list('0123456789')
letters_first_count = 2

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate_length = len(s)
    number_first_occuerance = False
    if any((c in punctuation_list) for c in s):
        return False
    if plate_length >= 2 and plate_length <= 6:
        for i in range(plate_length):
            if number_first_occuerance and s[i].lower() in alphabet:
                return False
            if i < letters_first_count and s[i].lower() not in alphabet:
                return False
            if s[i] == '0' and not number_first_occuerance:
                return False
            if s[i] in numbers:
                number_first_occuerance = True
        return True
    else:
        return False

main()
