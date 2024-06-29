#!/usr/bin/python3
INPUT_MSG = 'What time is it? '

def main():
    user_input = input(INPUT_MSG).strip().split()
    if len(user_input) == 2:
        if (user_input[1]) == 'pm':
            user_input_temp_list = user_input[0].split(':')
            user_input_temp_list[0] = str(int(user_input_temp_list[0]) + 12)
            user_input[0] = user_input_temp_list[0] + ':' + user_input_temp_list[1]
    time = convert(user_input[0])
    time_check_str = time_checker(time)
    if time_check_str is not None:
        print(time_check_str)

def time_checker(time: float):
    if time >= 7 and time <= 8:
        return('breakfast time')
    elif time >= 12 and time <= 13:
        return('lunch time')
    elif time >= 18 and time <= 19:
        return('dinner time')

def convert(time: str):
    hours, minutes = time.split(":")
    full_time = float(hours) + float(minutes) / 60
    return full_time


if __name__ == "__main__":
    main()
