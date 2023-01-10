#!/usr/bin/python3
import csv

FIELD_TO_REMOVE = 'heroname'

def main():
    with open('regularbirthday.csv', 'w', encoding="utf8") as out_f:
        with open('superbirthday.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            newfieldnames = [field for field in csv_reader.fieldnames if field != FIELD_TO_REMOVE]
            csv_writer = csv.DictWriter(out_f, newfieldnames)
            csv_writer.writeheader()
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                                  ## to do things
                    print('Column names are {}'.format(", ".join(row)))
                    line_count += 1
                # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
                # above is the python3.6+ way to do things
                print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
                line_count += 1
                row.pop(FIELD_TO_REMOVE)
                csv_writer.writerow(row)
    # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))
if __name__ == "__main__":
    main()

