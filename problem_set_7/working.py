import re

def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    matches = re.search(r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)', s)
    if not matches:
        raise ValueError('The format is not correct')
    if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
        raise ValueError('The hours are not in a logical limit')
    if matches.group(2) and matches.group(5):
        if int(matches.group(2)) >= 60 or int(matches.group(5)) >= 60:
            raise ValueError('The minutes are not in a logical limit')
    first_hours, first_minutes, first_type, second_hours, second_minutes, second_type = list(matches.groups())
    if first_type == 'PM':
        if first_hours != '12':
            first_hours = str(int(first_hours) + 12)
    if second_type == 'PM':
        if second_hours != '12':
            second_hours = str(int(second_hours) + 12)
    if first_type == 'AM' and first_hours == '12':
        first_hours = '00'
    if second_type == 'AM' and second_hours == '12':
        second_hours = '00'
    return f"{first_hours.zfill(2)}:{first_minutes if first_minutes is not None else '00'} to {second_hours.zfill(2)}:{second_minutes if second_minutes is not None else '00'}"

if __name__ == "__main__":
    main()
