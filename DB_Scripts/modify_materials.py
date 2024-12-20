import csv
import re


def process_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as infile, \
            open('../data/materialsM.csv', mode='w', newline='', encoding='utf-8') as outfile:

        reader = list(csv.reader(infile))
        read = reader[1:]
        writer = csv.writer(outfile)

        writer.writerow(reader[0])
        for index, row in enumerate(read):
            new_row = []
            row = row[0].split(';')
            new_row.append(index + 1)
            new_row.append(row[0])

            if row[1] == 'Гранулы':
                new_row.append(1)
            elif row[1] == 'Краски':
                new_row.append(2)
            elif row[1] == 'Нитки':
                new_row.append(3)
            else:
                new_row.append(row[1])

            if row[2].startswith("\\"):
                new_row.append(row[2])
            else:
                new_row.append("NULL")



            numbers = re.findall(r'\d+', row[3])
            if numbers:
                new_row.append(int(numbers[0]))
            else:
                new_row.append(0)


            numbers = re.findall(r'\d+', row[4])
            if numbers:
                new_row.append(int(numbers[0]))
            else:
                new_row.append(0)

            new_row.append(row[5])
            new_row.append(row[6])

            eighth_col_mapping = {'л': 1, 'м': 2, 'г': 3, 'кг': 4}
            new_row.append(eighth_col_mapping.get(row[7], row[7]))

            writer.writerow(new_row)


process_csv('../data/materials_k_import.csv')
