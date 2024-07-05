#!/usr/bin/python3
INPUT_MSG = 'Date: '
year_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input(INPUT_MSG)
    if ',' in date:
        splitted_date = date.split(',')
        day_month = splitted_date[0].split()
        month, day = day_month[0], day_month[1]
        try:
            if int(day) > 31:
                continue
        except ValueError:
            continue
        year = splitted_date[1].strip()
        try:
            month_index = str(year_months.index(month) + 1)
            print(f"{year}-{month_index.zfill(2)}-{day.zfill(2)}")
            break
        except ValueError:
            continue
    elif '/' in date:
        splitted_date = date.split('/')
        month, day, year = splitted_date[0], splitted_date[1], splitted_date[2]
        try:
            if int(month) > 12 or int(day) > 31:
                continue
        except ValueError:
            continue
        print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        break
    else:
        continue
