#!/usr/bin/python3

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    d = d[1:]
    return float(d)


def percent_to_float(p: str) -> float:
    p = p[:-1]
    return (float(p) / 100)

main()