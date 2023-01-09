#!/usr/bin/env python3
import os

IN_FILENAME = "dracula.txt"
OUT_FILENAME = "vampytimes.txt"
PATTERN = "vampire"


def main():
    """Write lines from the Dracula book containing the word 'vampire' to a file."""

    # Verify the file exists.
    if not os.path.exists(IN_FILENAME):
        print(f"Unable to find: {IN_FILENAME}")
        exit(1) # Unsuccessful exit status.

    with open(OUT_FILENAME, 'w', encoding='utf8') as out_file:
        # Count the number of occurrences of PATTERN within in_file.
        with open(IN_FILENAME, 'r', encoding='utf8') as in_file:
            count = 0
            for line in in_file:
                if PATTERN in line.lower():
                    # Output the matching line to the output file.
                    print(line, file=out_file, end="")
                    count += 1
            # Display number of matches found.
            print(f"Number of lines with {PATTERN} in them: {count}")

if __name__ == '__main__':
    main()
