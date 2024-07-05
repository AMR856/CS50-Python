#!/usr/bin/python3
items_dicts = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
INPUT_MSG = 'Item: '
OUTPUT_MSG = 'Total: '
total = 0
while True:
    try:
        item = input(INPUT_MSG).title()
        total += items_dicts[item]
        print(f'{OUTPUT_MSG}${total:.2f}')
        continue
    except KeyError:
        continue
    except EOFError:
        print()
        break
