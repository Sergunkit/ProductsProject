import csv
import re


def process_csv(file_path):
    with (open(file_path, mode='r', newline='', encoding='utf-8') as infile, \
            open('../data/supplierM.csv', mode='w', newline='', encoding='utf-8') as outfile):

        reader = list(csv.reader(infile))
        read = reader[1:]
        writer = csv.writer(outfile)

        writer.writerow(reader[0])
        for index, row in enumerate(read):
            new_row = []
            row = row[0].split(';')[0].split(', ')
            new_row.append(index + 1)
            new_row.append(row[0])

            if row[1] == 'МКК':
                new_row.append(1)
            elif row[1] == 'ОАО':
                new_row.append(2)
            elif row[1] == 'ООО':
                new_row.append(3)
            elif row[1] == 'ЗАО':
                new_row.append(4)
            elif row[1] == 'МФО':
                new_row.append(5)
            elif row[1] == 'ПАО':
                new_row.append(6)
            else:
                new_row.append(row[1])

            new_row.append(row[2])


            date = re.findall(r'\d+', row[3])
            if date:
                new_row.append(int(date[0]))
            else:
                new_row.append(0)

            matches = extract_date(row[4])
            if matches:
                new_row.append(matches)
            else:
                new_row.append('NULL')

            writer.writerow(new_row)



def extract_date(input_string):
    date_patterns = [
        r'\d{2}[.-]\d{2}[.-]\d{4}',  # dd.mm.yy или dd-mm-yy
        r'\d{4}-\d{2}-\d{2}',  # yyyy-mm-dd
        r'(\d{1,2})\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})\s*г?'
        # dd месяц yyyy
    ]
    month_mapping = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12'
    }


    for pattern in date_patterns:
        match = re.findall(pattern, input_string, flags=re.IGNORECASE)
        if not match:
            continue
        match = match[0]
        if len(match) == 3:
            day, month, year = match
            return f'{year}-{month_mapping[month]}-{day}'
        elif len(match) == 10 and match[2] == '.':
            day, month, year = match.split('.')
            return f'{year}-{month}-{day}'
        elif len(match) == 10 and match[4] == '-':
            year, month, day = match.split('-')
            return f'{year}-{month}-{day}'
        else:
            return None

process_csv('../data/supplier_k_import.csv')
