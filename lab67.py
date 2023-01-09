#!/usr/bin/env python3

IN_FILENAME = "dracula.txt"
OUT_FILENAME = "vampytimes.txt"
PATTERN = "vampire"

def main():
    with open(OUT_FILENAME, 'w', encoding='utf8') as out_file:
        with open(IN_FILENAME, 'r', encoding='utf8') as in_file:
            count = 0
            for line in in_file:
                if PATTERN in line.lower():
                    print(line, file=out_file, end="")
                    count += 1
            print(f"Number of lines with the {PATTERN} in them: {count}")

if __name__ == '__main__':
    main()
