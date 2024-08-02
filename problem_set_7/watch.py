#!/usr/bin/python3
import re

CHECKING_STRING_1 = 'www.youtube.com/embed'
CHECKING_STRING_2 = 'youtube.com/embed'
REPLACEMENT_STRING = 'youtu.be'


def main():
    print(parse(input("HTML: ")))

def parse(s: str) -> str:
    matches = re.search(r'src="(.+?)"', s)
    if matches:
        matched_string = matches.group(1)
        if 'youtube' not in matched_string:
            return None
        if 'www'in matched_string:
            matched_string = matched_string.replace(CHECKING_STRING_1, REPLACEMENT_STRING)
        else:
            matched_string = matched_string.replace(CHECKING_STRING_2, REPLACEMENT_STRING)
        if 'https' not in matched_string:
            matched_string = matched_string.replace('http', 'https')
        return matched_string

if __name__ == "__main__":
    main()
