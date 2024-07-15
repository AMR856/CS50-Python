#!/usr/bin/python3
import sys
import csv
import tabulate
if len(sys.argv) == 2:
    filename = sys.argv[1]
    first_time = False
    filename, extension = filename.split('.')
    if extension.lower() != 'csv':
        print('Not a CSV file')
        sys.exit(1)
    try:
        file_rows = []
        with open(f'{filename}.{extension}') as file:
            reader = csv.reader(file)
            for row in reader:
                if not first_time:
                    headers = row
                    first_time = True
                    continue
                file_rows.append(row)
            print(tabulate.tabulate(file_rows, headers=headers, tablefmt="grid"))
            sys.exit(0)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
else:
    print("Too few command-line arguments")
sys.exit(1)
