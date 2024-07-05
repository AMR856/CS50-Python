#!/usr/bin/python3
my_dict = {}
while True:
    try:
        user_input = input()
        my_dict[user_input.upper()] += 1
    except KeyError:
        my_dict[user_input.upper()] = 1
    except EOFError:
        myKeys = list(my_dict.keys())
        myKeys.sort()
        sorted_dict = {key: my_dict[key] for key in myKeys}
        for key, value in sorted_dict.items():
            print(f'{value} {key}')
        break
# check50 cs50/problems/2022/python/grocery
