#!/usr/bin/python3
import sys
# sys.argv[0] -> filename
file_length = 0
if len(sys.argv) == 2:
    filename = sys.argv[1]
    filename, extension = filename.split('.')
    if extension.lower() != 'py':
        print('Not a Python file')
        sys.exit(1)
    try:
        with open(f'{filename}.{extension}') as file:
            for line in file:
                if line.lstrip().rstrip() == '':
                    continue
                if line.lstrip()[0] == '#':
                    continue
                file_length += 1
            print(file_length)
            sys.exit(0)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
else:
    print("Too few command-line arguments")
sys.exit(1)
