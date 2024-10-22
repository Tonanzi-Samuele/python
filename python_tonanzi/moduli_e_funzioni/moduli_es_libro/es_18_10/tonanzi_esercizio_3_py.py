import tariffa as t

n_per = int(input("inserire numero persone:"))
litri_persone = int(input("inserire numero di litri per persona:"))

tariffa_base  = t.tariffa_base(n_per)
tariffa_litro = t.tariffa_raccolta(litri_persone)
som = t.somma(tariffa_base,tariffa_litro)
prezzo_con_iva = t.prezzo_iva(som)


print(f"""\
TARIFFA BASE = {tariffa_base}
TARIFFA LITRI = {tariffa_litro}
SOMMA =  {som}
PREZZO CON IVA = {prezzo_con_iva}""")