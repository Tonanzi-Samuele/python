import soldi


n = int(input("inserisci un numero "))
perc = float(input("inserisci una percentuale "))

for i in range(n):
    desc = str(input("inserire descrizione "))
    prezzo = float(input("inserire prezzo "))

    prezzo_aum = soldi.aumento(prezzo,perc)

soldi.stampa(prezzo_aum,desc)