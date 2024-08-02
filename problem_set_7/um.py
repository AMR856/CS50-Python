import re

def main():
    print(count(input("Text: ")))

def count(s: str) -> int:
    regex_pattern = re.compile(r'\bum\b', re.IGNORECASE)
    result = re.findall(regex_pattern, s)
    return len(result)

if __name__ == "__main__":
    main()
