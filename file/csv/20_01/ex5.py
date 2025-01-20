import csv 
from collections import defaultdict
try:
    with open("ex.csv",mode="r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
        
except FileNotFoundError:
    print("errore")