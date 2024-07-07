#!/usr/bin/python3
from queue import Queue
INPTU_MSG = "Name: "
DEFAULT_ADIEU = 'Adieu, adieu, to '
user_input_queue = Queue()
printed_before = False
while True:
    try:
        user_input_queue.put(input(INPTU_MSG))
    except EOFError:
        list_length = user_input_queue.qsize()
        print()
        print(DEFAULT_ADIEU, end='')
        while list_length > 0:
            if list_length == 1:
                if not printed_before:
                    print(user_input_queue.get())
                else:
                    print(f', and {user_input_queue.get()}')
            else:
                if not printed_before:
                    print(user_input_queue.get(), end='')
                else:
                    print(f', {user_input_queue.get()}', end='')
                printed_before = True
            list_length -= 1
        break

# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
