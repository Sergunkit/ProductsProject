import csv
import re


def process_csv(file_path1, file_path2, file_path3):
    with (open(file_path1, mode='r', newline='', encoding='utf-8') as infile1, \
          open(file_path2, mode='r', newline='', encoding='utf-8') as infile2, \
          open(file_path3, mode='r', newline='', encoding='utf-8') as infile3, \
          open('../data/material_supplierM.csv', mode='w', newline='', encoding='utf-8') as outfile):

        reader1 = list(csv.reader(infile1))
        mater = reader1[1:]

        reader2 = list(csv.reader(infile2))
        suppl = reader2[1:]

        reader3 = list(csv.reader(infile3))
        mat_sup = reader3[1:]

        writer = csv.writer(outfile)

        mater_d = {}
        for row in mater:
            mater_d[row[1]] = row[0]

        suppl_d = {}
        for row in suppl:
            suppl_d[row[1]] = row[0]

        for row in mat_sup:
            mat = row[0]
            sup = row[1]
            new_row = [mater_d[mat], suppl_d[sup]]
            writer.writerow(new_row)




process_csv('../data/materialsM.csv', '../data/supplierM.csv', '../data/materialsupplier_k_import.csv')
