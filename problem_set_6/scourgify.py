#!/usr/bin/python3
import sys
import csv

if len(sys.argv) == 3:
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    input_filename, input_extension = input_filename.split('.')
    output_filename, output_extension = output_filename.split('.')
    if input_extension != 'csv' or output_extension != 'csv':
        print("Not a CSV file")
        sys.exit(1)
    try:
        with open(f'{input_filename}.{input_extension}') as input_file, \
        open(f'{output_filename}.{output_extension}', 'w') as output_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in reader:
                name, house = row['name'], row['house']
                last, first = name.split(', ')
                writer.writerow({'first': first, 'last': last, 'house': house})
            sys.exit(0)
    except FileNotFoundError:
        print(f"Could not read {input_filename}.{input_extension}")
        sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
else:
    print("Too few command-line arguments")
sys.exit(1)
