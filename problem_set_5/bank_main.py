#!/usr/bin/python3
INPUT_MSG = 'Greeting: '

def main():
    greeting = input(INPUT_MSG)
    print(f'${value(greeting)}')

def value(greeting):
    greeting = greeting.strip().lower().split()
    if greeting[0].strip(',').strip('-') == 'hello':
        return 0
    elif greeting[0][0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
