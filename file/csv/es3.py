import csv

with open("ex.csv",mode="r",encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)