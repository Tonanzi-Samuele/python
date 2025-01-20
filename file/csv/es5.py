import csv

dati = [
    {'Nome': 'Tawney', 'Eta': '17', 'Citta': 'Nichelino'},
    {'Nome': 'Andrew', 'Eta': '17', 'Citta': 'Piossasco'},
    {'Nome': 'RickyOne', 'Eta': '17', 'Citta': 'Nichelino'},
    {'Nome': 'Trills', 'Eta': '3', 'Citta': 'Grugliasco'}
]

with open("diz.csv",mode="w",newline="",encoding="utf-8") as file:
    intestazione = ['Nome','Eta','Citta']
    writer = csv.DictWriter(file, fieldnames = intestazione)
    writer.writeheader()
    writer.writerows(dati)