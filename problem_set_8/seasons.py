#!/usr/bin/python3
from datetime import date, timedelta
import inflect
import re
import sys

INPUT_STR = 'Date of Birth: '
pattern = r'^\d{4}-\d{2}-\d{2}$'

p = inflect.engine()

def main():
    user_date = input(INPUT_STR)
    if is_valid(user_date):
        user_date = list(map(int, user_date.split('-')))
        timedelta_difference = get_difference(user_date)
        print(get_words_from_seconds(timedelta_difference))

def is_valid(str_input: str):
    if not re.match(pattern, str_input):
        print('Invalid date')
        sys.exit(1)
    return True

def get_difference(user_date: list):
    user_date = date(user_date[0], user_date[1], user_date[2])
    today_date = date.today()
    return today_date - user_date

def get_words_from_seconds(dif: timedelta):
    total_minutes = round(dif.total_seconds() / 60)
    return p.number_to_words(total_minutes, andword='').capitalize() + ' minutes'

if __name__ == "__main__":
    main()
