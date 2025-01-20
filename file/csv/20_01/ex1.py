import csv

with open("studenti.csv" , mode="w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome","Eta","Classe"])
    writer.writerow(["Tawney","17","1C"])
    writer.writerow(["Andrew","17","3B"])
    writer.writerow(["RickyOne","17","4D"])
    writer.writerow(["Trills","3","5A"])