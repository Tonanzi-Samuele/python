import csv
from collections import defaultdict
try: 
    with open("file1.csv", mode="a", encoding="utf-8" ) as file:
        writer = csv.writer(file)
        nuova_riga = ["BIGVROOM", "Gacha"]
        writer.writerow(nuova_riga)
        file.close()
    with open("file1.csv", mode = "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("errore")