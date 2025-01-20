import csv 
from collections import defaultdict

try:
    with open("prodotti.csv", mode ="a", encoding="utf-8") as file:
        writer = csv.writer(file)
        riga = ["Matita", 0.50, 300]
        writer.writerow(riga)
        file.close()
    with open("prodotti.csv",mode="r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
        
except FileNotFoundError:
    print("errore")