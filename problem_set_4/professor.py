import random
from typing import Tuple
LEVEL_MSG = 'Level: '
OUTPUT_MSG = 'Score: '

def main():
    user_level = get_level()
    levels_list = []
    user_score = 0
    available_tries = 3
    for i in range(10):
        first_num = generate_integer(user_level)
        second_num = generate_integer(user_level)
        passed_tuple = (first_num, second_num)
        levels_list.append((first_num, second_num))
        levels_list[i] = levels_list[i] + (equation_solver(passed_tuple),)
    for i in range(10):
        while available_tries:
            try:
                print(f'{levels_list[i][0]} + {levels_list[i][1]} = ', end='')
                user_answer = int(input())
                if user_answer == levels_list[i][2]:
                    user_score += 1
                    break
                else:
                    print('EEE')
                    available_tries -= 1
                    if available_tries == 0:
                        print(f'{levels_list[i][0]} + {levels_list[i][1]} = {levels_list[i][2]}', )
            except ValueError:
                available_tries -= 1
                print('EEE')
        available_tries = 3
    print(f'{OUTPUT_MSG}{user_score}')


def equation_solver(numbers_tuple: Tuple[int, int]) -> Tuple[int, ]:
    return numbers_tuple[0] + numbers_tuple[1]

def get_level() -> int:
    while True:
        try:
            user_level = int(input(LEVEL_MSG))
            if user_level in [1, 2, 3]:
                return user_level
            continue
        except ValueError:
            continue

def generate_integer(level: int) -> int:
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
