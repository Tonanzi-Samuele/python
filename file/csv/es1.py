import csv
from collections import defaultdict

def analizza_vendite(input_file,output_file):
    try:
        vendite_giorno = defaultdict(float)
        vendite_prodotto = defaultdict(int)
        
        with open(input_file, "r") as file: 
            reader = csv.DictReader(file)
            for riga in reader:
                data = riga["Data"]
                prodotto = riga["Prodotto"]
                quantita = riga["Quantita"]
                prezzo_unitario = float(riga["Prezzo_unitario"])

                tot_vendita = quantita * prezzo_unitario
                vendite_giorno[data] += tot_vendita
                vendite_prodotto[prodotto] += quantita

            prodotto_piu_venduto = max(vendite_prodotto,key=vendite_prodotto.get)
            quantita_piu_venduta = vendite_prodotto[prodotto_piu_venduto]
        
        with open(output_file,"w") as outfile:
            outfile.write("tot vendite per giorno: \n")
            for data, totale in vendite_giorno.items():
                outfile.write(f"{data}:{totale:.2f} €\n")
            outfile.write("\n")
            outfile.write("")


    except FileNotFoundError:
        print("file non trovato")


def main():
    analizza_vendite('vendite.csv','file.txt')
main()