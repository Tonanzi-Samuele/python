class Atleta:
    def __init__(self, nome = '', cognome = '', visitaMedica = True):
        self.nome = nome
        self.cognome = cognome
        self.visita = visitaMedica
        
    def pres(self):
        print(f"ciao sono {self.nome} {self.cognome} certificato: {'si' if self.visita == True else 'no'}")
