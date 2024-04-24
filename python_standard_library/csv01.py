import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "place"])
    writer.writerow(["john", 27, "chennai"])
    writer.writerow(["smith", 28, "usa"])
