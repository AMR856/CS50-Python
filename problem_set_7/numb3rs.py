#!/usr/bin/python3
import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip: str) -> bool:
    matches = re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip)
    if matches:
        segments = ip.split('.')
        if all([0 <= int(segment) <= 255 for segment in segments]):
            return True
    return False

if __name__ == "__main__":
    main()
