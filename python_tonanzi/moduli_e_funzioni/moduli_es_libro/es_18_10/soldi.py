def aumento(prezzo, p):
    prezzo = (prezzo * p)/100
    return prezzo

def stampa(prezzo_finale, d):
    print(f"""\
    descrizione - {d}
    prezzo aumentato - {prezzo_finale}""")
    