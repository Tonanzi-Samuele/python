class Prodotto():
    def __init__(self, nome = "", prezzo = 0 , quantita_disp = 5):

        self.nome = nome
        self.prezzo = prezzo
        self.quantita_disp = quantita_disp
    def getprezzo(self):
        return self.prezzo

class Ordine(Prodotto):
    def __init__(self, nome="", prezzo=0, quantita_disp =5, quantita_rich = 0):
        super().__init__(nome, prezzo, quantita_disp)
        self.somma = 0
        self.quantita_rich = quantita_rich
        self.prodotti = []
    def aggiungi_prodotti(self,prodotto,quantita_rich):
        self.prodotti.append([prodotto, quantita_rich])
        self.quantita_disp  = self.quantita_disp - self.quantita_rich
    def totale_ordine(self):
        for item in self.prodotti:
            prezzo = item[0].getprezzo()
            quantita = item[1]
            self.somma += prezzo * quantita
        return self.somma
    


def main():
    p1 = Prodotto("mouse", 3, 2)
    p2 = Prodotto("pc", 5, 2)
    ordine = Ordine()
    ordine.aggiungi_prodotti(p1, 1)
    ordine.aggiungi_prodotti(p2, 2)
    print(ordine.totale_ordine())

main()