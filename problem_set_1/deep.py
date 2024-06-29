#!/usr/bin/python3
INPUT_MSG = 'What is the Answer to the Great Question of Life, the Universe, and Everything? '
ACCEPTED_ANS = ['42', 'forty two', 'forty-two']
user_answer = input(INPUT_MSG).strip().lower()
if user_answer in ACCEPTED_ANS:
    print("YES")
else:
    print("NO")
