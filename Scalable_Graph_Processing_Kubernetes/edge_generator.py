
import csv

regions = dict()
with open('data/regions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            regions[row[0]] = row[1]
            line_count += 1
    print regions
