import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    content = list(reader)
    print(content)
