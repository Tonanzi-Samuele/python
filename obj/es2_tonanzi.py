class Atleta:
    def __init__(self, nome = '', cognome = '', visitaMedica = True):
        self.nome = nome
        self.cognome = cognome
        self.visita = visitaMedica
    def squadra(self, squad):
        self.squad = squad


    def pres(self):
        print(f"ciao sono {self.nome} {self.cognome} faccio parte della squadra {self.squad} certificato: {'si' if self.visita == True else 'no'}")
