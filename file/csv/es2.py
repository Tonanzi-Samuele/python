import csv

with open("ex.csv" , mode="w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome","Eta","Citta"])
    writer.writerow(["Tawney","17","Nichelino"])
    writer.writerow(["Andrew","17","Piossasco"])
    writer.writerow(["RickyOne","17","Nichelino"])
    writer.writerow(["Trills","3","Grugliasco"])