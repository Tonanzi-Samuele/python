codici= str(input("inserire codici: "))
codici = codici.split(',')
for codice in codici:
    codici_offuscati = ["****" + codice[4:]]
    print("Codici offuscati:")
for codice in codici_offuscati:
    print(codice)