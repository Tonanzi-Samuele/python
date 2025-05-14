class Libro():
    def __init__(self,titolo,autore,anno,pagine,editore,citta,soggetto,inPrestito = False):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.pagine = pagine
        self.editore = editore
        self.citta = citta
        self.soggetto = soggetto
        self.prestito = inPrestito

class Rivista(Libro):
    def __init__(self, titolo, autore, anno, pagine, editore, citta, soggetto, inPrestito=False, periodicita = ""):
        super().__init__(titolo, autore, anno, pagine, editore, citta, soggetto, inPrestito)
        self.periodicita = periodicita