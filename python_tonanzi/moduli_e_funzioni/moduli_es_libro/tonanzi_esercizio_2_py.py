n = int(input("inserisci un numero"))
perc = int(input("inserisci una percentuale"))

for i in range(n):
    desc = str(input("inserire descrizione"))
    prezzo = float(input("inserire prezzo"))

    prezzo_aum = soldi.aumento(prezzo,desc)
    soldi.stampa(prezzo_aum,desc)