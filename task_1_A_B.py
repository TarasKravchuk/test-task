import csv
import random
from string import ascii_letters, digits


def random_csv_file_creator (csv_file_name):
    csv_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(csv_file)
    data = [[''.join(random.sample(ascii_letters.join(digits), 8)) for i in range(0, 6)] for n in range(0, 1024)]
    for coloumn in data:
        writer.writerow(coloumn)
    csv_file.close()


def data_cleaner(csv_file_name, new_csv_file_name, digits=digits):
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
    result = []
    without_vowel = [row for row in data if all(elem not in [i for i in 'aAeEiIoOuU'] for elem in [i[0] for i in row])]
    for row in without_vowel:
        if any(i in [num for num in digits if int(num) % 2 != 0] for i in ''.join(row)):
            new_row = ''.join(row)
            for num in [num for num in digits if int(num) % 2 != 0]:
                new_row = new_row.replace(num, '#')
            result.append([(new_row[i:i+8]) for i in range(0, len(new_row), 8)])
        else:
            result.append(row)

    with open(new_csv_file_name, 'w') as new_csv_file:
        writer = csv.writer(new_csv_file)
        for coloumn in result:
            writer.writerow(coloumn)


random_csv_file_creator('/var/lib/mysql-files/test.csv')
data_cleaner('/var/lib/mysql-files/test.csv', '/var/lib/mysql-files/new_csv_file.csv')
