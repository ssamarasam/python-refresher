import csv

with open("roadmap.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count == 0):
            print("header: ", ','.join(row))
            line_count += 1
        else:
            print(f'\t course: {row[0]} platform: {row[1]} \n ')
            line_count += 1
