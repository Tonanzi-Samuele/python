import csv 
from collections import defaultdict
try:
    with open("studenti.csv",mode="r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("studenti 3A: ")
        for row in reader:
            if row["Classe"] == "3A":
                print(row["Nome"])
except FileNotFoundError:
    print("errore")      