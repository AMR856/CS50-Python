#!/usr/bin/python3
INSERT_MSG = 'Insert Coin: '
AMOUNG_MSG = 'Amount Due: '
FINISHED_MSG = 'Change Owed: '
ACCEPTED_COINS = [5, 10, 25]
coke_price = 50
while True:
    user_input = int(input(INSERT_MSG))
    if user_input not in  ACCEPTED_COINS:
        print(f'{AMOUNG_MSG}{coke_price}')
        continue
    coke_price = coke_price - user_input
    if coke_price > 0:
        print(f'{AMOUNG_MSG}{coke_price}')
    elif coke_price <= 0:
        break
print(f'{FINISHED_MSG}{abs(coke_price)}')
